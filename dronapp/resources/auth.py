from flask import Blueprint, request, jsonify
from flask import jsonify
from flask_login import  login_user
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import check_password_hash

from models.user import User
from extensions import db



auth_bp = Blueprint('auth', __name__)
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    role = data.get('role', 'observer')

    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'Username already exists!'}), 400

    new_user = User(username=username, role=role)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'Registration successful!'}), 201  

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user = User.query.filter_by(username=username).first()

    if user and check_password_hash(user.password_hash, password):
        login_user(user)
        access_token = create_access_token(identity=user.id)
       
        return jsonify({
            'status': 'success',
            'message': 'Logged in successfully',
            'access_token':access_token,  
            'role': user.role
        }), 200
    else:
        return jsonify({
            'status': 'error',
            'message': 'Invalid username or password'
        }), 401



@auth_bp.route('/role', methods=['GET'])
@jwt_required()
def get_role():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if user:
        return jsonify({'role': user.role}), 200
    else:
        return jsonify({'error': 'User not found'}), 404
@auth_bp.route('/logout', methods=['POST'])
def logout():
  
    return jsonify({'message': 'Logged out successfully'}), 200