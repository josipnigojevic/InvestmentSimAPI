from flask import Blueprint, jsonify, request
from Controllers.stock_controller import *

stock_routes = Blueprint('stock_routes', __name__)

@stock_routes.route('/<symbol>', methods=['GET'])
def get_stock(symbol):
    stock_data = get_stock_data(symbol)
    if stock_data:
        return jsonify(stock_data), 200
    return jsonify({'error': 'Stock not found'}), 404

@stock_routes.route('/<symbol>/historical', methods=['GET'])
def get_historical_stock(symbol):
    start_date = request.args.get('start')
    end_date = request.args.get('end')
    interval = request.args.get('interval', 'daily') 

    if not start_date or not end_date:
        return jsonify({'error': 'start and end dates are required'}), 400

    historical_data = get_historical_stock_data(symbol, start_date, end_date, interval)
    if historical_data:
        return jsonify(historical_data), 200
    return jsonify({'error': 'Historical data not found'}), 404

@stock_routes.route('/<symbol>/news', methods=['GET'])
def get_news(symbol):
    news_data = get_stock_news(symbol)
    if news_data:
        return jsonify(news_data), 200
    return jsonify({'error': 'News not found'}), 404

@stock_routes.route('/<symbol>/average_sentiment', methods=['GET'])
def get_average_sentiment_route(symbol):
    average_sentiment_data = get_average_sentiment(symbol)
    if average_sentiment_data:
        return jsonify(average_sentiment_data), 200
    return jsonify({'error': 'Sentiment data not found'}), 404

@stock_routes.route('/sp500/rank_by_sentiment', methods=['GET'])
def rank_sp500_by_sentiment_route():
    sentiment_rankings = rank_sp500_by_sentiment()
    return jsonify(sentiment_rankings), 200