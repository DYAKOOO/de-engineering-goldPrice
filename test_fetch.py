from data_sources import fetch_gold_price
from datetime import datetime

def test_fetch_gold_price():
    date_str = datetime.now().strftime('%Y%m%d')
    price_data = fetch_gold_price(date_str)
    print(f"Fetched price data for {date_str}: {price_data}")

if __name__ == "__main__":
    test_fetch_gold_price()