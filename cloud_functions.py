import os
import base64
import json
from google.cloud import bigquery
from google.cloud import storage
from google.cloud import pubsub_v1
import logging
import functions_framework
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Now you can access the variables like this:
project_id = os.getenv('GOOGLE_CLOUD_PROJECT')
dataset_id = os.getenv('BIGQUERY_DATASET')
table_id = os.getenv('BIGQUERY_TABLE')

# Use these variables in your BigQuery client setup, for example:
from google.cloud import bigquery

client = bigquery.Client(project=project_id)
table_ref = client.dataset(dataset_id).table(table_id)

logging.basicConfig(level=logging.INFO)

@functions_framework.cloud_event
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
        dataset = os.getenv('BIGQUERY_DATASET')
        table = os.getenv('BIGQUERY_TABLE')
        
        if not dataset or not table:
            logging.error("BIGQUERY_DATASET or BIGQUERY_TABLE environment variables are not set.")
            return 'Error: Missing BigQuery configuration', 500

        table_id = f"{os.getenv('PROJECT_ID')}.{dataset}.{table}"
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
    
    if not project_id or not topic_name:
        logging.error("PROJECT_ID or PUBSUB_TOPIC environment variables are not set.")
        return

    try:
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
    except Exception as e:
        logging.error(f"Error in main function: {str(e)}")

if __name__ == "__main__":
    main()