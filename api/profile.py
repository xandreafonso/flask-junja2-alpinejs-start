profile_bp_api = Blueprint('profile_api', __name__)

@profile_bp_api.route('/api/users/<code>')