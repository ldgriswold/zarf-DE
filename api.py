from flask import Flask, jsonify, request, render_template
import requests
import os

app = Flask(__name__)

app.secret_key = os.environ.get('SESSION_KEY', 'd3f417k3y5r0ck')

@app.route('/')
def index():
    return render_template('splash.html')

@app.route('/validate', methods=['POST'])
def validate():
    data = request.get_json()
    check_data(data)

if __name__ == '__main__':
    app.debug = True
    app.run()