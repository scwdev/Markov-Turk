import secrets
from flask import Flask, jsonify, request, json, Blueprint
from flask_sqlalchemy import SQLAlchemy
from app import db

import models.models as m

user = Blueprint('user', __name__)

# user.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://scwd:ofekdekel@localhost:5432/markov'

# db = SQLAlchemy(user)

def user_serializer(user):
    return {
        'id': user.id,
        'email': user.email,
        'api-key': user.api_key,
        'samples': user.samples,
        'date-created': user.date_created
    }

@user.route('/1', methods=['GET'])
def test():
    return '<h1> test 1 </h1>'

@user.route('/keys', methods=['GET'])
def index_users():
    return jsonify([*map(user_serializer, m.User.query.all())])

@user.route('/key/new', methods=['POST'])
def create_user():
    data = json.loads(request.data)
    user = m.User(email = data['email'], api_key=secrets.token_urlsafe(16))
    db.session.add(user)
    db.session.commit()

    return jsonify([*map(user_serializer, m.User.query.filter_by(email=data['email']))])

# checking if module is importing
print('views imported')