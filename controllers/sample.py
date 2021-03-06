from itertools import repeat

from flask import jsonify, request, json, Blueprint, g
from app import db

from models.sample import Sample
from controllers.utilities import key_check, mini_matrix_serializer

sample_bp = Blueprint('sample', __name__, url_prefix='/<api_key>')

@sample_bp.url_value_preprocessor
def handle_key(endpoints, values):
    api_key = values.pop('api_key')
    g.user = key_check(api_key)

@sample_bp.before_request
def check_key():
    if g.user == None:
        return jsonify({'status': 401, 'message': 'No such key.'})

def sample_serializer(sample):
    return {
        'id': sample.id,
        'user_id': sample.user_id,
        'sample_title': sample.sample_title,
        'initial_data': sample.initial_data,
        'added_data': sample.added_data,
        'matrices': [*map(mini_matrix_serializer, sample.matrices, repeat(g.user))],
        'created': sample.created,
        'updated': sample.updated
    }

@sample_bp.route('/sample', methods=['GET'])
def index_samples():
    return jsonify([*map(sample_serializer, Sample.query.filter_by(user_id=g.user.id).all())])

@sample_bp.route('/sample', methods=['POST'])
def create_sample():
    data = json.loads(request.data)

    if isinstance(data['initial_data'], list) == False:
        return jsonify({"status":400, "message": "please format 'initial_data' as an array of strings."})
    if sum(map(len,data['initial_data'])) > 1000000:
        return jsonify({"status":400, "message": "please confine training data to 1 million characters."})

    sample = Sample(
        user_id = g.user.id,
        sample_title = data['sample_title'],
        initial_data = [string.lower() for string in data['initial_data']],
        added_data = []
        )
    db.session.add(sample)
    db.session.commit()
    return jsonify({'status':'201', 'message': 'added new data successully'})


@sample_bp.route('/sample/<id>', methods=['GET', 'PUT', 'DELETE'])
def single_sample(id):
    sample = Sample.query.get(id)
    
    if sample.user_id != g.user.id:
        return jsonify({'status': '401', 'message': 'API is incorrect or does not exist.'})
    elif sample == None:
        return jsonify({'status': '400', 'message': 'no Sample at that id'})
    
    # Show route
    elif request.method == 'GET':
        return jsonify(sample_serializer(sample))
    
    # Update route
    elif request.method == 'PUT':
        data = json.loads(request.data)

        if isinstance(data['added_data'], list) == False:
            return jsonify({"status":400, "message": "please format 'added_data' as an array of strings."})
        
        if sum(map(len,data['added_data'])) > 1000000:
            return jsonify({"status":400, "message": "please confine added data to 1 million characters"})

        sample.added_data = data['added_data']
        sample.sample_title = data['sample_title']
        db.session.commit()
        return jsonify({"status": "204", "message": "Successfully updated"})
    
    # Destroy route
    elif request.method == 'DELETE':
        db.session.delete(sample)
        db.session.commit()
        return jsonify({"status": "204", "message": "Successfully deleted"})