import functions_framework
import logging

logging.basicConfig(level=logging.INFO)

@functions_framework.cloud_event
def process_pubsub(cloud_event):
    logging.info("Cloud Function triggered successfully!")
    return 'OK', 200