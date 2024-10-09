import os
import logging
from flask import Flask, jsonify
from google.cloud import pubsub_v1, storage
import json
from datetime import datetime
import requests


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Get environment variables
BASE_URL = os.environ.get('GOLD_API_BASE_URL', 'https://www.goldapi.io/api')
GOLD_API_KEY = os.environ.get('GOLD_API_KEY')
PROJECT_ID = os.environ.get('GOOGLE_CLOUD_PROJECT')
PUBSUB_TOPIC = os.environ.get('PUBSUB_TOPIC', 'gold-price')
GCS_BUCKET = os.environ.get('GCS_BUCKET', 'gold-price-raw-data')


def fetch_gold_price(date):
    url = f"{BASE_URL}/XAU/USD"
    headers = {'x-access-token': GOLD_API_KEY}
    
    logger.info(f"Fetching gold price from API for date: {date}")
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        logger.info(f"Received data: {data}")
        return {
            'date': date,
            'price': data.get('price'),
            'open_price': data.get('open_price'),
            'high_price': data.get('high_price'),
            'low_price': data.get('low_price')
        }
    except requests.RequestException as e:
        logger.error(f"Error fetching gold price data: {str(e)}")
        return None

def publish_to_pubsub(data):
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(PROJECT_ID, PUBSUB_TOPIC)
    
    data_str = json.dumps(data).encode("utf-8")
    try:
        future = publisher.publish(topic_path, data_str)
        message_id = future.result(timeout=30)
        logger.info(f"Published message ID: {message_id}")
        return True
    except Exception as e:
        logger.error(f"Error publishing to Pub/Sub: {str(e)}")
        return False


def write_to_gcs(data):
    client = storage.Client()
    bucket = client.bucket(GCS_BUCKET)
    blob = bucket.blob(f'gold_price_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json')
    blob.upload_from_string(json.dumps(data))
    logger.info(f"Data written to GCS: {blob.name}")

@app.route('/fetch-and-publish')
def fetch_and_publish():
    try:
        date_str = datetime.now().strftime('%Y-%m-%d')
        price_data = fetch_gold_price(date_str)
        if price_data:
            if publish_to_pubsub(price_data):
                write_to_gcs(price_data)  # Write to GCS after successful Pub/Sub publish
                return jsonify({"status": "success", "data": price_data}), 200
            else:
                return jsonify({"status": "error", "message": "Failed to publish to Pub/Sub"}), 500
        else:
            return jsonify({"status": "error", "message": "Failed to fetch gold price data"}), 500
    except Exception as e:
        logger.exception(f"An error occurred: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)