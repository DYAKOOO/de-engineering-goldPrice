import functions_framework
from google.cloud import storage
import json
import base64

@functions_framework.cloud_event
def process_pubsub(cloud_event):
    data = base64.b64decode(cloud_event.data["message"]["data"]).decode()
    gold_price_data = json.loads(data)
    
    # Process the data (e.g., write to BigQuery)
    # For now, let's just log it
    print(f"Received gold price data: {gold_price_data}")
    
    return 'OK'