from Services.user_service import *

def create_user_controller(data):
    username = data.get('username')
    email = data.get('email')
    if not username or not email:
        return {"error": "Username and email are required."}, 400
    
    user, error = create_user(username, email)
    if user:
        return user.to_dict(), 201
    return {"error": error}, 400

def delete_user_controller(user_id):
    success = delete_user(user_id)
    if success:
        return {"message": "User deleted successfully."}, 200
    return {"error": "User not found."}, 404

def get_user_controller(user_id):
    user = get_user(user_id)
    if user:
        return user, 200
    return {"error": "User not found."}, 404

def get_all_users_controller():
    users = get_all_users()
    return users, 200