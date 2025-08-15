
from flask import Blueprint

users_bp = Blueprint('users', __name__)

@users_bp.route('/users')
def list_users():
    return "Users list"

@users_bp.route('/users/<int:user_id>')
def show_user(user_id):
    return f"User {user_id}"
