
from flask import Blueprint, jsonify

profile_bp_api = Blueprint('profile_api', __name__)

@profile_bp_api.route('/api/profile')
def get(code):
    user_data = {
        'id': code,
        'name': f'User {code}',
        'email': f'user{code}@example.com'
    }
    return jsonify(user_data)
