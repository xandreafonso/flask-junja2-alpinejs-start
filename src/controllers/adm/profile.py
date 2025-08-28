from flask import Blueprint, render_template

profile_bp = Blueprint('adm_profile', __name__)

@profile_bp.route('/adm/profile')
def page():
    return render_template('adm/profile.html')
