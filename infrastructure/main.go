package main

import (
	"fmt"
	"github.com/pulumi/pulumi-gcp/sdk/v7/go/gcp/bigquery"
	"github.com/pulumi/pulumi-gcp/sdk/v7/go/gcp/pubsub"
	"github.com/pulumi/pulumi-gcp/sdk/v7/go/gcp/dataproc"
	"github.com/pulumi/pulumi-gcp/sdk/v7/go/gcp/cloudrun"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
	"github.com/pulumi/pulumi-gcp/sdk/v7/go/gcp/monitoring"
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

		// Create Pub/Sub topic
		topicName := "gold-price"
		topic, err := pubsub.NewTopic(ctx, topicName, &pubsub.TopicArgs{
			Name:    pulumi.String(topicName),
			Project: pulumi.String(project),
		}, pulumi.Import(pulumi.ID(fmt.Sprintf("projects/%s/topics/%s", project, topicName))))
		if err != nil {
			return err
		}


		// Create Pub/Sub subscription

		_, err = pubsub.NewSubscription(ctx, "gold-price-subscription", &pubsub.SubscriptionArgs{
			Name:    pulumi.String("gold-price-sub"),
			Topic:   topic.Name,
			Project: pulumi.String(project),
		}, pulumi.Import(pulumi.ID(fmt.Sprintf("projects/%s/subscriptions/gold-price-sub", project))))
		if err != nil {
			return err
		}

		// Create Dataproc cluster with reduced size
		dataprocCluster, err := dataproc.NewCluster(ctx, "spark-cluster", &dataproc.ClusterArgs{
			Name:    pulumi.String("gold-price-analysis-cluster"),
			Project: pulumi.String(project),
			Region:  pulumi.String(region),
			ClusterConfig: &dataproc.ClusterClusterConfigArgs{
				WorkerConfig: &dataproc.ClusterClusterConfigWorkerConfigArgs{
					NumInstances: pulumi.Int(2),
					MachineType:  pulumi.String("e2-medium"),
					DiskConfig: &dataproc.ClusterClusterConfigWorkerConfigDiskConfigArgs{
						BootDiskSizeGb: pulumi.Int(30),
					},
				},
				MasterConfig: &dataproc.ClusterClusterConfigMasterConfigArgs{
					NumInstances: pulumi.Int(1),
					MachineType:  pulumi.String("e2-medium"),
					DiskConfig: &dataproc.ClusterClusterConfigMasterConfigDiskConfigArgs{
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

		// Dataproc workflow template
		_, err = dataproc.NewWorkflowTemplate(ctx, "gold-price-analysis", &dataproc.WorkflowTemplateArgs{
			Project:  pulumi.String(project),
			Location: pulumi.String(region),
			Jobs: dataproc.WorkflowTemplateJobArray{
				&dataproc.WorkflowTemplateJobArgs{
					StepId: pulumi.String("clean_transform"),
					PysparkJob: &dataproc.WorkflowTemplateJobPysparkJobArgs{
						MainPythonFileUri: pulumi.String("gs://de-goldprice-code/spark_jobs/clean_transform.py"),
					},
				},
				&dataproc.WorkflowTemplateJobArgs{
					StepId: pulumi.String("load_to_bigquery"),
					PysparkJob: &dataproc.WorkflowTemplateJobPysparkJobArgs{
						MainPythonFileUri: pulumi.String("gs://de-goldprice-code/spark_jobs/load_to_bigquery.py"),
					},
				},
			},
			Placement: &dataproc.WorkflowTemplatePlacementArgs{
				ManagedCluster: &dataproc.WorkflowTemplatePlacementManagedClusterArgs{
					ClusterName: pulumi.String("gold-price-analysis-cluster"),
					Config: &dataproc.WorkflowTemplatePlacementManagedClusterConfigArgs{
						GceClusterConfig: &dataproc.WorkflowTemplatePlacementManagedClusterConfigGceClusterConfigArgs{
							Zone:    pulumi.String(zone),
							Network: pulumi.String("default"),
						},
					},
				},
			},
		})
		if err != nil {
			return err
		}

		// Create BigQuery dataset

		datasetName := "gold_price_dataset"
		dataset, err := bigquery.NewDataset(ctx, datasetName, &bigquery.DatasetArgs{
			DatasetId: pulumi.String(datasetName),
			Location:  pulumi.String("US"),
			Project:   pulumi.String(project),
		}, pulumi.Import(pulumi.ID(fmt.Sprintf("projects/%s/datasets/%s", project, datasetName))))
		if err != nil {
			return err
		}

		// Create BigQuery table
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
		}, pulumi.Import(pulumi.ID(fmt.Sprintf("projects/%s/datasets/%s/tables/gold_prices", project, datasetName))))

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
		}, pulumi.Import(pulumi.ID(fmt.Sprintf("projects/%s/datasets/%s/tables/gold_price_30day_avg", project, datasetName))))
		
		if err != nil {
			return err
		}

		// cloudrun new service
		_, err = cloudrun.NewService(ctx, "gold-price-ingestion", &cloudrun.ServiceArgs{
			Location: pulumi.String(region),
			Project:  pulumi.String(project),
			Template: &cloudrun.ServiceTemplateArgs{
				Spec: &cloudrun.ServiceTemplateSpecArgs{
					Containers: cloudrun.ServiceTemplateSpecContainerArray{
						&cloudrun.ServiceTemplateSpecContainerArgs{
							Image: pulumi.String("gcr.io/de-goldprice/gold-price-producer:v1.0.27"),
							Envs: cloudrun.ServiceTemplateSpecContainerEnvArray{
								&cloudrun.ServiceTemplateSpecContainerEnvArgs{
									Name:  pulumi.String("PUBSUB_TOPIC"),
									Value: topic.Name,
								},
								&cloudrun.ServiceTemplateSpecContainerEnvArgs{
									Name:  pulumi.String("GOOGLE_CLOUD_PROJECT"),
									Value: pulumi.String(project),
								},
								&cloudrun.ServiceTemplateSpecContainerEnvArgs{
									Name:  pulumi.String("GOLD_API_BASE_URL"),
									Value: pulumi.String("https://www.goldapi.io/api"),
								},
								&cloudrun.ServiceTemplateSpecContainerEnvArgs{
									Name:  pulumi.String("GOLD_API_KEY"),
									Value: pulumi.String("goldapi-1192n117m18se8at-io"), // Consider using a secret manager for this
								},
							},
							Ports: cloudrun.ServiceTemplateSpecContainerPortArray{
								&cloudrun.ServiceTemplateSpecContainerPortArgs{
									ContainerPort: pulumi.Int(8080),
								},
							},
						},
					},
				},
			},
		})


		// Create a Cloud Monitoring alert policy
		_, err = monitoring.NewAlertPolicy(ctx, "gold-price-alert", &monitoring.AlertPolicyArgs{
			DisplayName: pulumi.String("Gold Price Service Alert"),
			Combiner: pulumi.String("OR"),
			Conditions: monitoring.AlertPolicyConditionArray{
				&monitoring.AlertPolicyConditionArgs{
					DisplayName: pulumi.String("High error rate"),
					ConditionThreshold: &monitoring.AlertPolicyConditionConditionThresholdArgs{
						Filter: pulumi.String("resource.type = \"cloud_run_revision\" AND resource.labels.service_name = \"gold-price-ingestion\" AND metric.type = \"run.googleapis.com/request_count\" AND metric.labels.response_code_class = \"5xx\""),
						Duration:   pulumi.String("60s"),
						Comparison: pulumi.String("COMPARISON_GT"),
						ThresholdValue:  pulumi.Float64(5),
						Aggregations: monitoring.AlertPolicyConditionConditionThresholdAggregationArray{
							&monitoring.AlertPolicyConditionConditionThresholdAggregationArgs{
								AlignmentPeriod:  pulumi.String("60s"),
								PerSeriesAligner: pulumi.String("ALIGN_RATE"),
							},
						},
					},
				},
			},
		})
		if err != nil {
			return err
		}

		


		// Export resources
		ctx.Export("pubsubTopic", topic.Name)
		ctx.Export("dataprocClusterName", dataprocCluster.Name)
		ctx.Export("dataprocClusterRegion", dataprocCluster.Region)
		ctx.Export("bigQueryTableId", table.ID())


		return nil
	})
}
