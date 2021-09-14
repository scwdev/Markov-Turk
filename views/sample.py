from flask import Flask, jsonify, request, json
from flask_sqlalchemy import SQLAlchemy

import models as m

app = Flask('app')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://scwd:ofekdekel@localhost:5432/markov'

db = SQLAlchemy(app)

def sample_serializer(sample):
    return {
        'id': sample.id,
        'user_id': sample.user_id,
        'data_title': sample.data_title,
        'initial_data': sample.initial_data,
        'added_data': sample.added_data,
        'matrices': sample.matrices,
        'date_created': sample.date_created
    }


def key_check(api_key):
    user = m.User.query.filter_by(api_key=api_key).first()
    if user != None:
        return user


@app.route('/sample', methods=['GET'])
def sample_test():
    return '<h1> sample test </h1>'


@app.route('/data/<api_key>', methods=['GET'])
def index_data(api_key):
    user = key_check(api_key)
    
    return jsonify([*map(sample_serializer, m.Sample.query.filter_by(user_id=user.id).all())])


@app.route('/data/<api_key>', methods=['POST'])
def create_sample(api_key):
    user = m.User.query.filter_by(api_key=api_key).first()
    if user != None:
        data = json.loads(request.data)
        sample = m.Sample(
            user_id = user.id,
            data_title=data['data_title'],
            initial_data=data['initial_data']
            )
        db.session.add(sample)
        db.session.commit()

    return {'201' 'added new data successully'}


@app.route('/data/<api_key>/<id>', methods=['GET, PUT, DELETE'])
def single_sample(api_key, id):
    user = m.User.query.filter_by(api_key=api_key).first()
    if user != None:
        if request.method == 'GET':
            return jsonify([*map(
                sample_serializer,
        #         m.Sample.query.filter(user_id=user.id & id=id).first()
            )])
        # elif request.method == 'PUT':

        # elif request.method == 'DELETE':




# checking if module is importing
# print('views imported')