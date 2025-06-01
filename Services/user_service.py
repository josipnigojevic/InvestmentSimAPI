from Models.user_model import User, db

def create_user(username, email):
    existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
    if existing_user:
        return None, "Username or email already exists."
    
    new_user = User(username=username, email=email)
    db.session.add(new_user)
    db.session.commit()
    return new_user, None

def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return True
    return False

def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        return user.to_dict()
    return None

def get_all_users():
    users = User.query.all()
    return [user.to_dict() for user in users]