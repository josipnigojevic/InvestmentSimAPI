import requests
import logging

FRED_API_KEY = '6dcef40c4d1b695f8a202883d220d8e9'
FRED_BASE_URL = 'https://api.stlouisfed.org/fred/series/observations'

def get_economic_indicator_data(series_id):
    try:
        url = f"{FRED_BASE_URL}?series_id={series_id}&api_key={FRED_API_KEY}&file_type=json"
        logging.debug(f"Requesting economic indicator data from {url}")
        response = requests.get(url)
        data = response.json()
        
        logging.debug(f"FRED API response for {series_id}: {data}")
        
        if "observations" in data:
            return data["observations"]
        else:
            logging.error(f"No data found for series_id {series_id}")
            return None
    except Exception as e:
        logging.error(f"Error fetching economic indicator data for {series_id}: {e}")
        return None