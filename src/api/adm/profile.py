from flask import Blueprint, jsonify

profile_bp_api = Blueprint('adm_profile_api', __name__)

@profile_bp_api.route('/api/adm/profile')
def get():
    user_data = {
        'id': '123',
        'name': 'Alexandre Afonso',
        'email': 'eu@alexandreafonso.com.br'
    }
    return jsonify(user_data)