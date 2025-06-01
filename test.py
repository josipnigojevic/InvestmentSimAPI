import requests
import logging

API_KEY = 'CLAEK8R28SDAX19I'

logging.basicConfig(level=logging.DEBUG)

def get_historical_stock_prices(symbol, start_date, end_date, interval):
    function = 'TIME_SERIES_DAILY' if interval == 'daily' else \
               'TIME_SERIES_WEEKLY' if interval == 'weekly' else 'TIME_SERIES_MONTHLY'
    
    api_url = f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&apikey={API_KEY}'
    logging.debug(f"Requesting historical stock data from {api_url}")
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        logging.debug(f"Historical stock data response: {data}")
        
        if 'Error Message' in data:
            logging.error(f"Error from Alpha Vantage API: {data['Error Message']}")
            return None
        
        time_series_key = 'Time Series (Daily)' if interval == 'daily' else \
                          'Weekly Time Series' if interval == 'weekly' else 'Monthly Time Series'
        
        if time_series_key in data:
            time_series = data[time_series_key]
            filtered_data = {date: info for date, info in time_series.items() if start_date <= date <= end_date}
            logging.debug(f"Filtered historical data: {filtered_data}")
            return filtered_data
        else:
            logging.error(f"Time series key not found in response: {data}")
    else:
        logging.error(f"Failed to fetch historical data: {response.status_code}")
    
    return None

symbol = 'IBM'
start_date = '2023-01-01'
end_date = '2023-06-01'
interval = 'daily'

historical_data = get_historical_stock_prices(symbol, start_date, end_date, interval)
if historical_data:
    print(historical_data)
else:
    print("No historical data found.")
