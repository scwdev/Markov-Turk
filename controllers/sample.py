from flask import jsonify, request, json, Blueprint
from app import db

from models.sample import Sample
from controllers.utilities import key_check

sample_bp = Blueprint('sample', __name__)

def sample_serializer(sample):
    return {
        'id': sample.id,
        'user_id': sample.user_id,
        'data_title': sample.data_title,
        'initial_data': json.loads(sample.initial_data),
        # TODO needs an if statement for json.loads...
        'added_data': sample.added_data,
        'matrices': sample.matrices,
        'created': sample.created,
        'updated': sample.updated
    }

@sample_bp.route('/sample', methods=['GET'])
def sample_test():
    return '<h1> sample test </h1>'


@sample_bp.route('/data/<api_key>', methods=['GET'])
def index_data(api_key):
    user = key_check(api_key)
    if user == None:
        return jsonify({'status': '401', 'message': 'API is incorrect or does not exist.'})
    else:
        return jsonify([*map(sample_serializer, Sample.query.filter_by(user_id=user.id).all())])


@sample_bp.route('/data/<api_key>', methods=['POST'])
def create_sample(api_key):
    user = key_check(api_key)
    if user == None:
        return jsonify({'status': '401', 'message': 'API is incorrect or does not exist.'})
    else:
        data = json.loads(request.data)
        sample = Sample(
            user_id = user.id,
            data_title = data['data_title'],
            initial_data = json.dumps(data['initial_data'])
            )
        db.session.add(sample)
        db.session.commit()
        return jsonify({'status':'201', 'message': 'added new data successully'})


@sample_bp.route('/data/<api_key>/<id>', methods=['GET', 'PUT', 'DELETE'])
def single_sample(api_key, id):
    # test if api_key matches a user
    user = key_check(api_key)
    # query sample by primary_key number
    sample = Sample.query.get(id)
    if user == None:
        return jsonify({'status': '401', 'message': 'API is incorrect or does not exist.'})
    # Show route
    elif request.method == 'GET':
        print(sample)
        return jsonify(sample_serializer(sample))
    # Update route
    elif request.method == 'PUT':
        data = json.loads(request.data)
        sample.added_data = json.dumps(data['added_data'])
        sample.data_title = data['data_title']
        db.session.commit()
        # TODO needs return statement
    # Destroy route
    elif request.method == 'DELETE':
        db.session.delete(sample)
        db.session.commit()
        # TODO needs return statement
