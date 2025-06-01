from flask import Blueprint, jsonify, request
from Controllers.portfolio_controller import *

portfolio_routes = Blueprint('portfolio_routes', __name__)

@portfolio_routes.route('/portfolio/<int:user_id>/create', methods=['POST'])
def create_portfolio_route(user_id):
    return jsonify(*create_user_portfolio(user_id))

@portfolio_routes.route('/portfolio/<int:user_id>/buy', methods=['POST'])
def buy_stock_route(user_id):
    symbol = request.json.get('symbol')
    shares = request.json.get('shares')
    if not symbol or not shares:
        return jsonify({"error": "Symbol and shares are required."}), 400
    return jsonify(*buy_stock(user_id, symbol, int(shares)))

@portfolio_routes.route('/portfolio/<int:user_id>/sell', methods=['POST'])
def sell_stock_route(user_id):
    symbol = request.json.get('symbol')
    shares = request.json.get('shares')
    if not symbol or not shares:
        return jsonify({"error": "Symbol and shares are required."}), 400
    return jsonify(*sell_stock(user_id, symbol, int(shares)))

@portfolio_routes.route('/portfolio/<int:user_id>', methods=['GET'])
def get_portfolio_route(user_id):
    return jsonify(*get_portfolio(user_id))

@portfolio_routes.route('/portfolio/<int:user_id>/value', methods=['GET'])
def get_portfolio_value_route(user_id):
    return jsonify(*get_portfolio_total_value(user_id))