from flask import Blueprint, jsonify, request
from Controllers.analytics_controller import get_stock_technical_analysis

analytics_routes = Blueprint('analytics_routes', __name__)

@analytics_routes.route('/analytics/<string:symbol>', methods=['GET'])
def get_technical_analysis_route(symbol):
    period = request.args.get('period', '1y')  
    return jsonify(*get_stock_technical_analysis(symbol, period))