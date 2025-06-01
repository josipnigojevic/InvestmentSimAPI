from flask import Blueprint, jsonify
from Controllers.market_controller import get_market_index_information

market_routes = Blueprint('market_routes', __name__)

@market_routes.route('/market/<string:symbol>', methods=['GET'])
def get_market_index_route(symbol):
    return jsonify(*get_market_index_information(symbol))