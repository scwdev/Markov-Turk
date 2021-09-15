import secrets
from flask import Flask, jsonify, request, json, Blueprint
from app import db

from models.user import User

user_bp = Blueprint('user', __name__)

def user_serializer(user):
    return {
        'id': user.id,
        'email': user.email,
        'api_key': user.api_key,
        'samples': user.samples,
        'created': user.created,
        'updated': user.updated
    }

@user_bp.route('/1', methods=['GET'])
def test():
    return '<h1> test 1 </h1>'

@user_bp.route('/keys', methods=['GET'])
def index_users():
    return jsonify([*map(user_serializer, User.query.all())])

@user_bp.route('/key/new', methods=['POST'])
def create_user():
    data = json.loads(request.data)
    user = User(email = data['email'], api_key=secrets.token_urlsafe(16))
    db.session.add(user)
    db.session.commit()

    return jsonify([*map(user_serializer, User.query.filter_by(email=data['email']))])

# checking if module is importing
print('views imported')