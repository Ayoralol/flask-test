from flask import request, jsonify, current_app as app # type: ignore
from . import db
from .models import User

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password_hash = data.get('password_hash')

    if not username or not email or not password_hash:
        return jsonify({'error': 'Missing data'}), 400

    new_user = User(username=username, email=email, password_hash=password_hash)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User added'}), 201

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'id': user.id, 'username': user.username, 'email': user.email} for user in users])
