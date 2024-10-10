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

@app.route('/fetch-and-publish')
def fetch_and_publish():
    try:
        logger.info(f"GOLD_API_KEY: {'*' * (len(GOLD_API_KEY) - 4) + GOLD_API_KEY[-4:] if GOLD_API_KEY else 'Not set'}")
        logger.info(f"BASE_URL: {BASE_URL}")
        
        url = f"{BASE_URL}/XAU/USD"
        headers = {'x-access-token': GOLD_API_KEY}
        
        logger.info(f"Fetching gold price from API")
        logger.info(f"Request URL: {url}")
        logger.info(f"Request Headers: {headers}")
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        logger.info(f"API Response: {data}")
        
        return jsonify({"status": "success", "data": data}), 200
    except requests.RequestException as e:
        logger.error(f"Error fetching gold price data: {str(e)}")
        logger.error(f"Response status code: {e.response.status_code if e.response else 'N/A'}")
        logger.error(f"Response content: {e.response.content if e.response else 'N/A'}")
        return jsonify({"status": "error", "message": str(e)}), 500
    except Exception as e:
        logger.exception(f"An unexpected error occurred: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)