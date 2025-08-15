from flask import Flask, render_template

app = Flask(__name__, static_folder='static', static_url_path='/static')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ping')
def hello():
    return 'pong'

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
