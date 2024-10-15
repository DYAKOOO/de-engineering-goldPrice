import os
import logging
from flask import Flask, jsonify
from google.cloud import pubsub_v1, storage
import json
from datetime import datetime
import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

BASE_URL = os.environ.get('GOLD_API_BASE_URL', 'https://www.goldapi.io/api')
GOLD_API_KEY = os.environ.get('GOLD_API_KEY')
PROJECT_ID = os.environ.get('GOOGLE_CLOUD_PROJECT')
PUBSUB_TOPIC = os.environ.get('PUBSUB_TOPIC', 'gold-price')
GCS_BUCKET = os.environ.get('GCS_BUCKET', 'gold-price-raw-data')

def fetch_gold_price(date):
    url = f"{BASE_URL}/XAU/USD"
    headers = {'x-access-token': GOLD_API_KEY}
    
    logger.info(f"Fetching gold price from API for date: {date}")
    logger.info(f"URL: {url}")
    logger.info(f"Headers: {headers}")
    
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
        logger.error(f"Response status code: {getattr(e.response, 'status_code', 'N/A')}")
        logger.error(f"Response content: {getattr(e.response, 'content', 'N/A')}")
        return None



def write_to_gcs(data):
    client = storage.Client()
    bucket = client.bucket(GCS_BUCKET)
    blob = bucket.blob(f'gold_price_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json')
    blob.upload_from_string(json.dumps(data))
    logger.info(f"Data written to GCS: {blob.name}")
    
@app.route('/')
def home():
    return jsonify({"status": "ok", "message": "Gold Price Ingestion Service is running"}), 200

@app.route('/fetch-and-publish')
def fetch_and_publish():
    try:
        logger.info(f"GOLD_API_KEY: {'*' * (len(GOLD_API_KEY) - 4) + GOLD_API_KEY[-4:] if GOLD_API_KEY else 'Not set'}")
        logger.info(f"BASE_URL: {BASE_URL}")
        
        date_str = datetime.now().strftime('%Y-%m-%d')
        gold_price_data = fetch_gold_price(date_str)
        
        if gold_price_data:
            # Write to GCS
            write_to_gcs(gold_price_data)
            
            # Publish to Pub/Sub
            publisher = pubsub_v1.PublisherClient()
            topic_path = publisher.topic_path(PROJECT_ID, PUBSUB_TOPIC)
            data_str = json.dumps(gold_price_data).encode("utf-8")
            future = publisher.publish(topic_path, data_str)
            message_id = future.result(timeout=30)
            logger.info(f"Published message ID: {message_id}")
            
            return jsonify({"status": "success", "data": gold_price_data}), 200
        else:
            return jsonify({"status": "error", "message": "Failed to fetch gold price data"}), 500
    except Exception as e:
        logger.exception(f"An unexpected error occurred: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 500

def publish_to_pubsub(topic_name, data):
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(PROJECT_ID, topic_name)
    data_str = json.dumps(data).encode("utf-8")
    try:
        future = publisher.publish(topic_path, data_str)
        message_id = future.result(timeout=30)
        logger.info(f"Published message ID: {message_id}")
        return True
    except Exception as e:
        logger.error(f"Error publishing to Pub/Sub: {str(e)}")
        return False
        
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)
    logger.info(f"Application starting on port {port}")