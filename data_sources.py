import requests
import pandas as pd
from datetime import datetime, timedelta
import os



API_KEY = os.getenv('GOLD_API_KEY')
FRED_API_KEY = os.getenv('FRED_API_KEY')
ALPHA_VANTAGE_API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')

#Gold Price Data
BASE_URL = 'https://www.goldapi.io/api'

def fetch_gold_price(date):
    url = f"{BASE_URL}/XAU/USD/{date}"
    headers = {'x-access-token': API_KEY}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return {
            'date': data.get('date', date),  # Use the input date if 'date' is not in the response
            'price': data.get('price'),
            'open': data.get('open_price'),
            'high': data.get('high_price'),
            'low': data.get('low_price')
        }
    else:
        print(f"Error fetching gold price data for {date}: {response.status_code}")
        return None
        
def fetch_central_bank_data(date):
    url = f"https://api.stlouisfed.org/fred/series/observations?series_id=FEDFUNDS&observation_start={date}&api_key={FRED_API_KEY}&file_type=json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            'date': date,
            'federal_funds_rate': float(data['observations'][-1]['value'])
        }
    else:
        print(f"Error fetching central bank data for {date}: {response.status_code}")
        return None

def fetch_mining_data(date):
    # As an example, we'll use Alpha Vantage to fetch stock data for a major gold mining company
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=NEM&apikey={ALPHA_VANTAGE_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            'date': date,
            'newmont_stock_price': float(data['Global Quote']['05. price'])
        }
    else:
        print(f"Error fetching mining data for {date}: {response.status_code}")
        return None

def fetch_market_data(date):
    # We'll use Alpha Vantage again to fetch S&P 500 data as a market indicator
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=SPY&apikey={ALPHA_VANTAGE_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            'date': date,
            'sp500_price': float(data['Global Quote']['05. price'])
        }
    else:
        print(f"Error fetching market data for {date}: {response.status_code}")
        return None


def main():
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)  # Fetch last 30 days of data
    
    data = []
    current_date = start_date
    while current_date <= end_date:
        date_str = current_date.strftime('%Y%m%d')
        price_data = fetch_gold_price(date_str)
        if price_data:
            data.append(price_data)
        current_date += timedelta(days=1)
    
    df = pd.DataFrame(data)
    df.to_csv('gold_prices.csv', index=False)
    print(f"Data saved to gold_prices.csv")

if __name__ == "__main__":
    main()