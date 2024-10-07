import os
import base64
import json
from google.cloud import bigquery
from google.cloud import storage
from google.cloud import pubsub_v1
import logging

logging.basicConfig(level=logging.INFO)

def process_pubsub(event, context):
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    logging.info(f"Received message: {pubsub_message}")

    try:
        message_data = json.loads(pubsub_message)
        
        # Store raw data in Cloud Storage
        storage_client = storage.Client()
        bucket = storage_client.bucket('gold-price-raw-data')
        blob = bucket.blob(f"gold_price_{message_data['date']}.json")
        blob.upload_from_string(pubsub_message)
        logging.info(f"Raw data stored in Cloud Storage: {blob.name}")
        
        # Insert data into BigQuery
        client = bigquery.Client()
        table_id = f"{os.getenv('PROJECT_ID')}.{os.getenv('BIGQUERY_DATASET')}.{os.getenv('BIGQUERY_TABLE')}"

        errors = client.insert_rows_json(table_id, [message_data])
        if errors == []:
            logging.info("New rows have been added to BigQuery.")
        else:
            logging.error(f"Encountered errors while inserting rows: {errors}")
    
    except Exception as e:
        logging.error(f"Error processing message: {str(e)}")
    
    return 'Ok' , 200

def main():
    project_id = os.getenv('PROJECT_ID')
    topic_name = os.getenv('PUBSUB_TOPIC')

    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_name)

    # Fetch gold price data here
    data = {"date": "2023-04-10", "price": 1950.5}  # Replace with actual data fetching

    # Publish to Pub/Sub
    future = publisher.publish(topic_path, json.dumps(data).encode('utf-8'))
    message_id = future.result()
    logging.info(f"Published message with ID: {message_id}")

    # Process the data
    process_pubsub({'data': base64.b64encode(json.dumps(data).encode('utf-8'))}, None)

if __name__ == "__main__":
    main()