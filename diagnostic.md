## Storage 
```bash
gcloud storage ls
gsutil ls gs://your-bucket-name  # List contents of a specific bucket
```


## Bigquery 

```bash
bq ls  # List datasets
bq ls your_dataset  # List tables in a dataset
bq show your_dataset.your_table  # Show table details`
```

## Pubsub 

```bash 
gcloud pubsub topics list
gcloud pubsub subscriptions list
```

## Cloud Run 

```bash
gcloud pubsub topics list
gcloud pubsub subscriptions list
```

### Cloud run logs 
```bash 
gcloud run services logs read gold-price-ingestion --region=us-west1
```

### Cloud run endpoint(s)
```bash
[IN] SERVICE_URL=$(gcloud run services describe gold-price-ingestion --region=us-west1 --format='value(status.url)')
[IN] curl ${SERVICE_URL}
{"message":"Gold Price Ingestion Service is running","status":"ok"}
[IN] curl ${SERVICE_URL}/fetch-and-publish
{"data":{"date":"2024-10-15","high_price":2652.855,"low_price":2645.465,"open_price":2648.96,"price":2646.825},"status":"success"}
```

## Compute Engine 

```bash
gcloud compute instances list
gcloud compute instances describe spark-instance --zone=us-west1-a
```

## Cloud Composer 

```bash
gcloud compute instances list
gcloud compute instances describe spark-instance --zone=us-west1-a
```

## IAM 

```bash
gcloud projects get-iam-policy your-project-id
gcloud iam service-accounts list
```


## Compute Engine (Spark)

```bash
gcloud compute ssh spark-instance --zone=us-west1-a --command="sudo journalctl -u google-startup-scripts.service"
```

## BigQuery 

```bash
bq query --use_legacy_sql=false 'SELECT COUNT(*) FROM `de-goldprice.gold_price_dataset.gold_prices`'
bq query --use_legacy_sql=false 'SELECT * FROM `de-goldprice.gold_price_dataset.gold_prices` LIMIT 5'
```
## GCS

```bash
gsutil cat gs://gold-price-raw-data/some_file.json | head -n 20
```

### Configure Docker to use gcloud as a credential helper:
```bash
gcloud auth configure-docker
```
