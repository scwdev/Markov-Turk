import secrets

from flask import Flask, jsonify, request, json, Blueprint
from app import db

from models.user import User
from controllers.utilities import key_check

user_bp = Blueprint('user', __name__)

def user_serializer(user):
    return {
        'id': user.id,
        'email': user.email,
        'api_key': user.api_key,
        'samples': [*map(sample_serializer, user.samples)],
        'matrices': [*map(matrix_serializer, user.matrices)],
        'outputs': [*map(output_serializer, user.outputs)],
        'created': user.created,
        'updated': user.updated
    }

def sample_serializer(sample):
    return {
        'sample_id': sample.id,
        'sample_title': sample.sample_title
    }
def matrix_serializer(matrix):
    return {
        'matrix_id': matrix.id,
        'matrix_title': matrix.matrix_title
    }
def output_serializer(output):
    return {
        'output_id': output.id,
        'output_title': output.output_title
    }

## Temporary, remove before deploy.
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