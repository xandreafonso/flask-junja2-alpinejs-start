import os
from flask import Flask, render_template
from src.db import db
from dotenv import load_dotenv

from src.api.public.login import login_bp_api

from src.api.adm.users import users_bp_api
from src.api.adm.profile import profile_bp_api
from src.api.adm.posts import posts_bp_api

from src.controllers.adm.dashboard import dashboard_bp
from src.controllers.adm.profile import profile_bp
from src.controllers.adm.posts import posts_bp

load_dotenv(".env.production" if os.getenv("FLASK_ENV") == "production" else None)

app = Flask(__name__, static_folder='static', static_url_path='/static')

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(login_bp_api)

app.register_blueprint(users_bp_api)
app.register_blueprint(profile_bp_api)
app.register_blueprint(posts_bp_api)

app.register_blueprint(dashboard_bp)
app.register_blueprint(profile_bp)
app.register_blueprint(posts_bp)


@app.route('/ping')
def ping():
    return 'pong'


@app.route('/')
def home():
    return render_template('public/home.html')


@app.route('/login')
def login():
    return render_template('public/login.html')


@app.context_processor
def template_vars():
    return {'version': '0.0.1'}


def main():
    app.run(port=int(os.environ.get('PORT', 80)))


if __name__ == "__main__":
    main()
