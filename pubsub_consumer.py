from google.cloud import pubsub_v1
import json
from google.cloud import storage
from datetime import datetime
import os

PROJECT_ID = os.getenv('GCP_PROJECT_ID')
if not PROJECT_ID:
    raise ValueError("GCP_PROJECT_ID environment variable is not set")
SUBSCRIPTION_NAME = 'gold-prices-sub'
BUCKET_NAME = 'gold-price-raw-data'

subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(PROJECT_ID, SUBSCRIPTION_NAME)

storage_client = storage.Client()
bucket = storage_client.bucket(BUCKET_NAME)

def store_in_gcs(data):
    date_str = datetime.now().strftime('%Y%m%d_%H%M%S')
    blob = bucket.blob(f'gold_price_{date_str}.json')
    blob.upload_from_string(json.dumps(data))
    print(f"Stored data in GCS: gs://{BUCKET_NAME}/{blob.name}")

def callback(message):
    print(f"Received message: {message.data}")
    data = json.loads(message.data)
    store_in_gcs(data)
    message.ack()

def main():
    streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
    print(f"Listening for messages on {subscription_path}")

    try:
        streaming_pull_future.result()
    except Exception as e:
        streaming_pull_future.cancel()
        print(f"Listening for messages has stopped: {e}")

if __name__ == "__main__":
    main()