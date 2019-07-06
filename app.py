from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index'

@app.route('/hello')
def hello():
    return 'Hello'

@app.route('/user/<username>')
def show_user(username):
    return 'Hello %s' % username

@app.route('/id/<int:user_id>')
def show_user_id(user_id):
    return 'User id %d' % user_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return 'Subpath %s' % subpath

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)