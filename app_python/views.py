from flask import render_template, request, jsonify, url_for, flash, redirect

from app import app
from login_aut import login_users
from register import register
from data import users


@app.route('/')
def start():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['user']
        password = request.form['password']
        try:
            return login_users(users, username, password)
        except:
           return 'erro ao loggar' 
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register_app():
    if request.method == 'POST':
        new_user = request.form['new_user']
        new_password = request.form['new_password']
        new_screen = request.form['new_screen']
        register(new_user, new_password, new_screen)
    return render_template('register.html')

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.get_json()

    if 'leitura' in data:
        reader = data['leitura']
        print(f'receive: {reader}')
        return jsonify(
            {
                "status": "success",
                "reader": reader 
            }
        ), 200
    else:
        return jsonify(
            {
                "status": "error",
                "message": "data not found"
            }
        ), 400