import secrets
from itertools import repeat

from flask import Flask, jsonify, request, json, Blueprint
from app import db

from models.user import User
from controllers.utilities import key_check, mini_matrix_serializer, mini_output_serializer, mini_sample_serializer

user_bp = Blueprint('user', __name__)

def user_serializer(user):
    return {
        'id': user.id,
        'email': user.email,
        'api_key': user.api_key,
        'samples': [*map((mini_sample_serializer), user.samples, repeat(user))],
        'matrices': [*map(mini_matrix_serializer, user.matrices, repeat(user))],
        'outputs': [*map(mini_output_serializer, user.outputs , repeat(user))],
        'created': user.created,
        'updated': user.updated
    }

## TODO -- Temporary, remove before deploy.
@user_bp.route('/keys', methods=['GET'])
def index_users():
    user = User.query.get(1)
    return jsonify([*map(user_serializer, User.query.all())])

@user_bp.route('/key/new', methods=['POST'])
def create_user():
    data = json.loads(request.data)
    user = User(email = data['email'], api_key=secrets.token_urlsafe(16))
    db.session.add(user)
    db.session.commit()
    return jsonify([*map(user_serializer, User.query.filter_by(email=data['email']))])

@user_bp.route('/user/<api_key>', methods=['GET', 'PUT','DELETE'])
def modify_user(api_key):
    user = key_check(api_key)
    if user == None:
        return jsonify({'status': 401, 'message': 'no such key'})
    elif request.method == 'GET':

        return jsonify(user_serializer(user))
    elif request.method == 'PUT':
        data = json.loads(request.data)
        user.email = data['email']
        db.session.commit()
        return jsonify({'status': 200, "message": 'email updated'})
    elif request.method == 'DELETE':
        db.session.delete(user)
        db.session.commit()
        return jsonify({'status': 200, "message": 'All user data, training data, probability matrices, and saved outputs deleted.'})