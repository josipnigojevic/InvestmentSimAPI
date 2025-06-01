from flask import Blueprint, jsonify
from Controllers.company_controller import get_company_information

company_routes = Blueprint('company_routes', __name__)

@company_routes.route('/company/<string:symbol>', methods=['GET'])
def get_company_info_route(symbol):
    return jsonify(*get_company_information(symbol))