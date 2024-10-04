package main

import (
	"encoding/base64"
	"fmt"
	"os"
	"os/exec"  // exec package
    "github.com/pulumi/pulumi-gcp/sdk/v7/go/gcp/bigquery"
	"github.com/pulumi/pulumi-gcp/sdk/v7/go/gcp/container"
	"github.com/pulumi/pulumi-gcp/sdk/v7/go/gcp/pubsub"
	"github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes"
	appsv1 "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/apps/v1"
	corev1 "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/core/v1"
	metav1 "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/meta/v1"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
	"github.com/pulumi/pulumi-gcp/sdk/v7/go/gcp/dataproc"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Load configuration
		conf := config.New(ctx, "")
		project := conf.Get("project")
		if project == "" {
			project = "de-goldprice"
		}
		region := conf.Get("region")
		if region == "" {
			region = "us-west1"
		}
		zone := conf.Get("zone")
		if zone == "" {
			zone = "us-west1-a"
		}

		// Load service account key
		serviceAccountKeyPath := os.Getenv("GOOGLE_APPLICATION_CREDENTIALS")
		if serviceAccountKeyPath == "" {
			return fmt.Errorf("GOOGLE_APPLICATION_CREDENTIALS environment variable is not set")
		}

		serviceAccountKey, err := os.ReadFile(serviceAccountKeyPath)
		if err != nil {
			return fmt.Errorf("failed to read service account key file: %v", err)
		}

		// Create GKE cluster with a new name
		cluster, err := container.NewCluster(ctx, "gold-price-cluster-pulumi", &container.ClusterArgs{
			Project:               pulumi.String(project),
			Location:              pulumi.String(zone),
			InitialNodeCount:      pulumi.Int(1),
			DeletionProtection:    pulumi.Bool(false),
			RemoveDefaultNodePool: pulumi.Bool(true),
		})

		if err != nil {
			return err
		}

		// Create node pool
		_, err = container.NewNodePool(ctx, "primary-node-pool", &container.NodePoolArgs{
			Cluster:   cluster.Name,
			Location:  pulumi.String(zone),
			Project:   pulumi.String(project),
			NodeCount: pulumi.Int(1),
			NodeConfig: &container.NodePoolNodeConfigArgs{
				MachineType: pulumi.String("e2-small"),
				OauthScopes: pulumi.StringArray{
					pulumi.String("https://www.googleapis.com/auth/cloud-platform"),
					pulumi.String("https://www.googleapis.com/auth/devstorage.read_only"),
				},
			},
			Autoscaling: &container.NodePoolAutoscalingArgs{
				MinNodeCount: pulumi.Int(1),
				MaxNodeCount: pulumi.Int(3),
			},
			Management: &container.NodePoolManagementArgs{
				AutoRepair:  pulumi.Bool(true),
				AutoUpgrade: pulumi.Bool(true),
			},
		})
		if err != nil {
			return err
		}

		// Create Kubernetes provider
		k8sProvider, err := kubernetes.NewProvider(ctx, "k8s-provider", &kubernetes.ProviderArgs{
			Kubeconfig: pulumi.All(cluster.Name, cluster.Endpoint, pulumi.String(project), pulumi.String(zone)).ApplyT(
				func(args []interface{}) (string, error) {
					clusterName := args[0].(string)
					endpoint := args[1].(string)
					project := args[2].(string)
					zone := args[3].(string)
					return getKubeconfig(clusterName, endpoint, project, zone)
				}).(pulumi.StringOutput),
		}, pulumi.DependsOn([]pulumi.Resource{cluster}))
		if err != nil {
			return err
		}

		// Create Pub/Sub topic
		topic, err := pubsub.NewTopic(ctx, "gold-prices-topic", &pubsub.TopicArgs{
			Name:    pulumi.String("gold-prices"),
			Project: pulumi.String(project),
		})
		if err != nil {
			return err
		}

		// Create Pub/Sub subscription
		_, err = pubsub.NewSubscription(ctx, "gold-prices-subscription", &pubsub.SubscriptionArgs{
			Name:    pulumi.String("gold-prices-sub"),
			Topic:   topic.Name,
			Project: pulumi.String(project),
		})
		if err != nil {
			return err
		}

		// Create secret for service account key
		secret, err := corev1.NewSecret(ctx, "pubsub-key", &corev1.SecretArgs{
			Metadata: &metav1.ObjectMetaArgs{
				Name: pulumi.String("pubsub-key"),
			},
			Data: pulumi.StringMap{
				"key.json": pulumi.String(base64.StdEncoding.EncodeToString(serviceAccountKey)),
			},
		}, pulumi.Provider(k8sProvider))
		if err != nil {
			return err
		}
		// Create Gold price consumer deployment
		_, err = appsv1.NewDeployment(ctx, "gold-price-consumer", &appsv1.DeploymentArgs{
			Metadata: &metav1.ObjectMetaArgs{
				Name: pulumi.String("gold-price-consumer"),
			},
			Spec: &appsv1.DeploymentSpecArgs{
				Replicas: pulumi.Int(1),
				Selector: &metav1.LabelSelectorArgs{
					MatchLabels: pulumi.StringMap{
						"app": pulumi.String("gold-price-consumer"),
					},
				},
				Template: &corev1.PodTemplateSpecArgs{
					Metadata: &metav1.ObjectMetaArgs{
						Labels: pulumi.StringMap{
							"app": pulumi.String("gold-price-consumer"),
						},
					},
					Spec: &corev1.PodSpecArgs{
						Containers: corev1.ContainerArray{
							&corev1.ContainerArgs{
								Name:  pulumi.String("gold-price-consumer"),
								Image: pulumi.String("gcr.io/" + project + "/gold-price-consumer:v1.0.0"), // Use a specific version tag
								Env: corev1.EnvVarArray{
									&corev1.EnvVarArgs{
										Name:  pulumi.String("PUBSUB_SUBSCRIPTION"),
										Value: pulumi.String("gold-prices-sub"),
									},
									&corev1.EnvVarArgs{
										Name:  pulumi.String("GOOGLE_APPLICATION_CREDENTIALS"),
										Value: pulumi.String("/var/secrets/google/key.json"),
									},
								},
								VolumeMounts: corev1.VolumeMountArray{
									&corev1.VolumeMountArgs{
										Name:      pulumi.String("google-cloud-key"),
										MountPath: pulumi.String("/var/secrets/google"),
									},
								},
							},
						},
						Volumes: corev1.VolumeArray{
							&corev1.VolumeArgs{
								Name: pulumi.String("google-cloud-key"),
								Secret: &corev1.SecretVolumeSourceArgs{
									SecretName: secret.Metadata.Name().Elem(),
								},
							},
						},
					},
				},
			},
		}, pulumi.Provider(k8sProvider))
		if err != nil {
			return err
		}


		// Create Dataproc cluster
		dataprocCluster, err := dataproc.NewCluster(ctx, "spark-cluster", &dataproc.ClusterArgs{
			Name:    pulumi.String("gold-price-analysis-cluster"),
			Project: pulumi.String(project),
			Region:  pulumi.String(region),
			ClusterConfig: &dataproc.ClusterClusterConfigArgs{
				MasterConfig: &dataproc.ClusterClusterConfigMasterConfigArgs{
					NumInstances: pulumi.Int(1),
					MachineType:  pulumi.String("n1-standard-2"),
					DiskConfig: &dataproc.ClusterClusterConfigMasterConfigDiskConfigArgs{
						BootDiskSizeGb: pulumi.Int(30),
					},
				},
				WorkerConfig: &dataproc.ClusterClusterConfigWorkerConfigArgs{
					NumInstances: pulumi.Int(2),
					MachineType:  pulumi.String("n1-standard-2"),
					DiskConfig: &dataproc.ClusterClusterConfigWorkerConfigDiskConfigArgs{
						BootDiskSizeGb: pulumi.Int(30),
					},
				},
				SoftwareConfig: &dataproc.ClusterClusterConfigSoftwareConfigArgs{
					ImageVersion: pulumi.String("2.0-debian10"),
				},
			},
		})
		if err != nil {
			return err
		}

		// Create BigQuery dataset
		dataset, err := bigquery.NewDataset(ctx, "gold_price_dataset", &bigquery.DatasetArgs{
			DatasetId: pulumi.String("gold_price_dataset"),
			Location:  pulumi.String("US"), // or your preferred location
			Project:   pulumi.String(project),
		})
		if err != nil {
			return err
		}
		table, err := bigquery.NewTable(ctx, "gold_prices", &bigquery.TableArgs{
			DatasetId: dataset.DatasetId,
			TableId:   pulumi.String("gold_prices"),
			Project:   pulumi.String(project),
			Schema: pulumi.String(`[
				{
					"name": "date",
					"type": "DATE",
					"mode": "REQUIRED"
				},
				{
					"name": "price",
					"type": "FLOAT",
					"mode": "REQUIRED"
				},
				{
					"name": "open_price",
					"type": "FLOAT",
					"mode": "NULLABLE"
				},
				{
					"name": "high_price",
					"type": "FLOAT",
					"mode": "NULLABLE"
				},
				{
					"name": "low_price",
					"type": "FLOAT",
					"mode": "NULLABLE"
				}
			]`),
			TimePartitioning: &bigquery.TableTimePartitioningArgs{
				Type:  pulumi.String("DAY"),
				Field: pulumi.String("date"),
			},
			// Remove the Clustering field for now
		})
		if err != nil {
			return err
		}
	
		// Create a view for 30-day moving average
		_, err = bigquery.NewTable(ctx, "gold_price_30day_avg", &bigquery.TableArgs{
			DatasetId: dataset.DatasetId,
			TableId:   pulumi.String("gold_price_30day_avg"),
			Project:   pulumi.String(project),
			View: &bigquery.TableViewArgs{
				Query: pulumi.Sprintf(`
					SELECT
						date,
						price,
						AVG(price) OVER (ORDER BY date ROWS BETWEEN 29 PRECEDING AND CURRENT ROW) AS moving_avg_30day
					FROM
						%s.%s.gold_prices
					ORDER BY
						date DESC
				`, project, dataset.DatasetId),
				UseLegacySql: pulumi.Bool(false),
			},
		})
		if err != nil {
			return err
		}
		


	

		// Export Kubernetes cluster name and endpoint
		ctx.Export("k8sClusterName", cluster.Name)
		ctx.Export("k8sClusterEndpoint", cluster.Endpoint)
	
		// Export pub sub topic
		ctx.Export("pubsubTopic", topic.Name)

		// Export dataproc cluster name , endpoint 
		ctx.Export("dataprocClusterName", dataprocCluster.Name)
		ctx.Export("dataprocClusterRegion", dataprocCluster.Region)

		// Export BigQuery table ID
		ctx.Export("bigQueryTableId", table.ID())



	

		return nil
	})
}

func getKubeconfig(clusterName, endpoint, project, zone string) (string, error) {
	cmd := exec.Command("gcloud", "container", "clusters", "get-credentials", clusterName,
		"--zone", zone, "--project", project)
	kubeconfig, err := cmd.Output()
	if err != nil {
		return "", err
	}
	return string(kubeconfig), nil
}