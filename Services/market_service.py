import yfinance as yf
import logging

def get_market_index_data(symbol):
    try:
        market_index = yf.Ticker(symbol)
        info = market_index.info
        

        history = market_index.history(period="1d")
        history.index = history.index.strftime('%Y-%m-%d %H:%M:%S')  
        
        logging.debug(f"Market index data for {symbol}: {info}")
        return {
            "info": info,
            "history": history.to_dict(orient='index')  
        }
    except Exception as e:
        logging.error(f"Error fetching market index data for {symbol}: {e}")
        return None