import functions_framework
from google.cloud import storage
import json
import base64
import logging
import sys

# Set up logging
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(__name__)

@functions_framework.cloud_event
def process_pubsub(cloud_event):
    logger.debug("Function started")
    try:
        data = base64.b64decode(cloud_event.data["message"]["data"]).decode()
        gold_price_data = json.loads(data)
        logger.info(f"Received gold price data: {gold_price_data}")
        # Process the data (e.g., write to BigQuery)
        return ('', 204)
    except Exception as e:
        logger.error(f"Error processing message: {str(e)}")
        return (str(e), 500)

# This line is crucial for Gen 2 functions
process_pubsub = functions_framework.cloud_event(process_pubsub)