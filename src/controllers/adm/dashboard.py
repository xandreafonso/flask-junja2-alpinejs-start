from flask import Blueprint, render_template

dashboard_bp = Blueprint('adm_dashboard', __name__)

@dashboard_bp.route('/adm/dashboard')
def page():
    return render_template('adm/dashboard.html')
