
from flask import Blueprint, render_template

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/profile')
def page():
    return render_template('pages/profile.html')
