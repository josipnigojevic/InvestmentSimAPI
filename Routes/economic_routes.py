from flask import Blueprint, jsonify
from Controllers.economic_controller import get_economic_indicator_information

economic_routes = Blueprint('economic_routes', __name__)

@economic_routes.route('/economic/<string:series_id>', methods=['GET'])
def get_economic_indicator_route(series_id):
    return jsonify(*get_economic_indicator_information(series_id))