
from flask import Blueprint, jsonify

login_bp_api = Blueprint('login_api', __name__)

@login_bp_api.route('/api/login', methods=['POST'])
def login():
    user_data = {
        'id': '123',
        'name': 'Alexandre Afonso',
        'email': 'eu@alexandreafonso.com.br'
    }
    return jsonify(user_data)
