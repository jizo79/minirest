from flask import Flask, request, render_template
import os
import socket

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/user/<username>')
def show_user(username):
    return 'Hello %s' % username

@app.route('/id/<int:user_id>')
def show_user_id(user_id):
    return 'User id %d' % user_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return 'Subpath %s' % subpath

@app.route('/git')
def show_build_from_git():
    return 'Correctly build from git!'

@app.route('/method', methods=['GET', 'POST'])
def route_different_method():
    if request.method == 'POST':
        return 'By POST'
    elif request.method == 'GET':
        return 'By GET'
    else:
        return 'By something else'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)