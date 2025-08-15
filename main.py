from flask import Flask, render_template, request

app = Flask(__name__, static_folder='static', static_url_path='/static')

@app.route('/ping')
def ping():
    return 'pong'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard')
def dashboard():
    return render_template('pages/dashboard.html')

@app.route('/profile')
def profile():
    return render_template('pages/profile.html')

@app.context_processor
def template_vars():
    return { 'version': '1.0.0' }

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
