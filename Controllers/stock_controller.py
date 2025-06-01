from Models.stock_model import Stock
from Services.stock_service import *
from Services.news_service import *
from sp500 import SP500_SYMBOLS
import logging

def get_stock_data(symbol):
    stock_data = get_real_time_stock_price(symbol)
    if stock_data:
        stock = Stock(symbol, stock_data['price'], stock_data['timestamp'])
        return stock.to_dict()
    logging.error(f"No real-time stock data found for {symbol}")
    return None

def get_historical_stock_data(symbol, start_date, end_date, interval):
    historical_data = get_historical_stock_prices(symbol, start_date, end_date, interval)
    if historical_data:
        return historical_data
    logging.error(f"No historical data found for {symbol} from {start_date} to {end_date} with interval {interval}")
    return None

def get_stock_news(symbol):
    news_data = get_financial_news_with_sentiment(symbol)
    if news_data:
        return news_data
    logging.error(f"No news found for {symbol}")
    return None

def get_average_sentiment(symbol):
    news_data = get_financial_news_with_sentiment(symbol)
    if not news_data:
        logging.error(f"No news found for {symbol}")
        return None
    
    total_compound = sum(article['sentiment']['compound'] for article in news_data)
    average_compound = total_compound / len(news_data)
    
    return {
        "symbol": symbol,
        "average_compound_sentiment": average_compound,
        "number_of_articles": len(news_data)
    }

def rank_sp500_by_sentiment():
    sentiment_scores = []
    for symbol in SP500_SYMBOLS:
        sentiment_data = get_average_sentiment(symbol)
        if sentiment_data:
            sentiment_scores.append(sentiment_data)
    
    sentiment_scores.sort(key=lambda x: x['average_compound_sentiment'], reverse=True)
    return sentiment_scores