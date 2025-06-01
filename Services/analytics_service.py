import yfinance as yf
import pandas_ta as ta
import logging
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

def get_technical_indicators(symbol, period="1y"):
    try:

        stock_data = yf.TTicker(symbol)
        history = stock_data.history(period=period)

        history['SMA_20'] = ta.sma(history['Close'], length=20)
        history['SMA_50'] = ta.sma(history['Close'], length=50)
        
        history['RSI'] = ta.rsi(history['Close'], length=14)
        
        macd = ta.macd(history['Close'])
        history['MACD'] = macd['MACD_12_26_9']
        history['MACD_Signal'] = macd['MACDs_12_26_9']
        
        bbands = ta.bbands(history['Close'], length=20, std=2)
        history['BB_upper'] = bbands['BBU_20_2.0']
        history['BB_middle'] = bbands['BBM_20_2.0']
        history['BB_lower'] = bbands['BBL_20_2.0']
        
        logging.debug(f"Historical data with indicators: {history.tail()}")

        predictions = predict_future_prices(history['Close'])

        prediction_df = pd.DataFrame(predictions, columns=['Predicted_Close'])
        
        history.index = history.index.strftime('%Y-%m-%d')

        historical_data = history.to_dict(orient='index')
        future_predictions = prediction_df.to_dict(orient='index')

        return {
            "historical_data": historical_data,
            "future_predictions": future_predictions
        }

    except Exception as e:
        logging.error(f"Error fetching technical indicators for {symbol}: {e}")
        return None

def predict_future_prices(close_prices):
    try:

        close_prices = close_prices.dropna()  
        X = np.arange(len(close_prices)).reshape(-1, 1)  
        y = close_prices.values  


        model = LinearRegression()
        model.fit(X, y)

        future_days = 5
        future_X = np.arange(len(close_prices), len(close_prices) + future_days).reshape(-1, 1)
        predictions = model.predict(future_X)
        

        last_date = close_prices.index[-1]
        future_dates = pd.date_range(start=last_date, periods=future_days+1, freq='B')[1:]  
        
        predicted_series = pd.Series(predictions, index=future_dates)
        
        return predicted_series
    except Exception as e:
        logging.error(f"Error in predictive analysis: {e}")
        return None
