from data_sources import fetch_gold_price, fetch_central_bank_data, fetch_mining_data, fetch_market_data
from pubsub_producer import publish_to_pubsub
from datetime import datetime
from cloud_functions import process_pubsub

def main():
    date_str = datetime.now().strftime('%Y%m%d')
    
    # Fetch data from various sources
    gold_price_data = fetch_gold_price(date_str)
    central_bank_data = fetch_central_bank_data(date_str)
    mining_data = fetch_mining_data(date_str)
    market_data = fetch_market_data(date_str)
    
    # Publish data to Pub/Sub
    if gold_price_data:
        publish_to_pubsub('gold-prices', gold_price_data)
    if central_bank_data:
        publish_to_pubsub('central-bank-data', central_bank_data)
    if mining_data:
        publish_to_pubsub('mining-data', mining_data)
    if market_data:
        publish_to_pubsub('market-data', market_data)

if __name__ == "__main__":
    main()
    process_pubsub(None)