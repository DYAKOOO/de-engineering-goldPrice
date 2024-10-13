package main

import (
	"github.com/pulumi/pulumi-gcp/sdk/v7/go/gcp/bigquery"
	"github.com/pulumi/pulumi-gcp/sdk/v7/go/gcp/pubsub"
	"github.com/pulumi/pulumi-gcp/sdk/v7/go/gcp/compute"
	"github.com/pulumi/pulumi-gcp/sdk/v7/go/gcp/cloudrun"
	"github.com/pulumi/pulumi-gcp/sdk/v7/go/gcp/storage"
	"github.com/pulumi/pulumi-gcp/sdk/v7/go/gcp/composer"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
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

		// Import existing buckets
		rawDataBucket, err := storage.NewBucket(ctx, "gold-price-raw-data", &storage.BucketArgs{
			Name:     pulumi.String("gold-price-raw-data"),
			Location: pulumi.String("US"),
			Project:  pulumi.String(project),
		}, pulumi.Import(pulumi.ID("gold-price-raw-data")))
		if err != nil {
			return err
		}

		processedDataBucket, err := storage.NewBucket(ctx, "gold-price-processed-data", &storage.BucketArgs{
			Name:     pulumi.String("gold-price-processed-data"),
			Location: pulumi.String("US"),
			Project:  pulumi.String(project),
		}, pulumi.Import(pulumi.ID("gold-price-processed-data")))
		if err != nil {
			return err
		}

		codeBucket, err := storage.NewBucket(ctx, "de-goldprice-code", &storage.BucketArgs{
			Name:     pulumi.String("de-goldprice-code"),
			Location: pulumi.String("US"),
			Project:  pulumi.String(project),
		}, pulumi.Import(pulumi.ID("de-goldprice-code")))
		if err != nil {
			return err
		}

		// Create Pub/Sub topic
		topicName := "gold-price"
		topic, err := pubsub.NewTopic(ctx, topicName, &pubsub.TopicArgs{
			Name:    pulumi.String(topicName),
			Project: pulumi.String(project),
		})
		if err != nil {
			return err
		}

		// Create Pub/Sub subscription
		_, err = pubsub.NewSubscription(ctx, "gold-price-subscription", &pubsub.SubscriptionArgs{
			Name:    pulumi.String("gold-price-sub"),
			Topic:   topic.Name,
			Project: pulumi.String(project),
		})
		if err != nil {
			return err
		}

		// Create a Compute Engine instance for Spark
		sparkInstance, err := compute.NewInstance(ctx, "spark-instance", &compute.InstanceArgs{
			Name:        pulumi.String("spark-instance"),
			MachineType: pulumi.String("n1-standard-4"),
			Zone:        pulumi.String(zone),
			BootDisk: &compute.InstanceBootDiskArgs{
				InitializeParams: &compute.InstanceBootDiskInitializeParamsArgs{
					Image: pulumi.String("ubuntu-os-cloud/ubuntu-2004-lts"),
				},
			},
			NetworkInterfaces: compute.InstanceNetworkInterfaceArray{
				&compute.InstanceNetworkInterfaceArgs{
					Network: pulumi.String("default"),
					AccessConfigs: compute.InstanceNetworkInterfaceAccessConfigArray{
						&compute.InstanceNetworkInterfaceAccessConfigArgs{},
					},
				},
			},
			Metadata: pulumi.StringMap{
				"startup-script": pulumi.String(`
					#!/bin/bash
					apt-get update
					apt-get install -y openjdk-11-jdk
					wget https://archive.apache.org/dist/spark/spark-3.1.2/spark-3.1.2-bin-hadoop3.2.tgz
					tar xvf spark-3.1.2-bin-hadoop3.2.tgz
					mv spark-3.1.2-bin-hadoop3.2 /opt/spark
					echo "export PATH=$PATH:/opt/spark/bin" >> /etc/environment
				`),
			},
			Tags: pulumi.StringArray{
				pulumi.String("spark"),
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
		})
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
		})
		if err != nil {
			return err
		}

		// Cloud Run service
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

		// Create Cloud Composer environment
		_, err = composer.NewEnvironment(ctx, "gold-price-composer", &composer.EnvironmentArgs{
			Name:     pulumi.String("gold-price-composer"),
			Region:   pulumi.String(region),
			Project:  pulumi.String(project),
			Config: &composer.EnvironmentConfigArgs{
				SoftwareConfig: &composer.EnvironmentConfigSoftwareConfigArgs{
					ImageVersion: pulumi.String("composer-3-airflow-2.9.3"),
				},
			},
		})
		if err != nil {
			return err
		}

		// Export resources
		ctx.Export("pubsubTopic", topic.Name)
		ctx.Export("sparkInstanceName", sparkInstance.Name)
		ctx.Export("sparkInstanceIP", sparkInstance.NetworkInterfaces.Index(pulumi.Int(0)).AccessConfigs().Index(pulumi.Int(0)).NatIp())
		ctx.Export("bigQueryTableId", table.ID())
		ctx.Export("rawDataBucketName", rawDataBucket.Name)
		ctx.Export("processedDataBucketName", processedDataBucket.Name)
		ctx.Export("codeBucketName", codeBucket.Name)

		return nil
	})
}