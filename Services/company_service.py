import yfinance as yf
import logging

def get_company_info(symbol):
    try:
        company = yf.Ticker(symbol)
        info = company.info
        logging.debug(f"Company information for {symbol}: {info}")
        return info
    except Exception as e:
        logging.error(f"Error fetching company information for {symbol}: {e}")
        return None