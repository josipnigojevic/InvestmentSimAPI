from flask import Blueprint, jsonify, request
from Controllers.user_controller import *

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/users', methods=['POST'])
def create_user_route():
    data = request.get_json()
    return jsonify(*create_user_controller(data))

@user_routes.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user_route(user_id):
    return jsonify(*delete_user_controller(user_id))

@user_routes.route('/users/<int:user_id>', methods=['GET'])
def get_user_route(user_id):
    return jsonify(*get_user_controller(user_id))

@user_routes.route('/users', methods=['GET'])
def get_all_users_route():
    return jsonify(*get_all_users_controller())