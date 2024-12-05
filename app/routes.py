from flask import Blueprint, jsonify
from .models import User

main = Blueprint('main', __name__)

@main.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    
    users_data = [
        {"id": user.id, "name": user.name, "email": user.email}
        for user in users
    ]
    
    return jsonify(users_data)