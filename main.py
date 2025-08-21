from flask import Flask, render_template
from api.profile import profile_bp_api
from api.login import login_bp_api
from controllers.dashboard import dashboard_bp
from controllers.profile import profile_bp

app = Flask(__name__, static_folder='static', static_url_path='/static')

app.register_blueprint(login_bp_api)
app.register_blueprint(profile_bp_api)

app.register_blueprint(dashboard_bp)
app.register_blueprint(profile_bp)


@app.route('/ping')
def ping():
    return 'pong'


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login')
def login():
    return render_template('pages/login.html')


@app.context_processor
def template_vars():
    return {'version': '0.0.1'}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
