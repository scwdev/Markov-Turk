from flask import jsonify, request, json, Blueprint, g
from app import db

from models.sample import Sample
from controllers.user import matrix_serializer
from controllers.utilities import key_check

sample_bp = Blueprint('sample', __name__, url_prefix='/<api_key>')

@sample_bp.url_value_preprocessor
def print_endpoints(endpoints, values):
    api_key = values.pop('api_key')
    g.user = key_check(api_key)
    if g.user == None:
        return jsonify({'status': '401', 'message': 'API is incorrect or does not exist.'})

def sample_serializer(sample):
    return {
        'id': sample.id,
        'user_id': sample.user_id,
        'sample_title': sample.sample_title,
        'initial_data': sample.initial_data,
        'added_data': sample.added_data,
        'matrices': [*map(matrix_serializer, sample.matrices)],
        'created': sample.created,
        'updated': sample.updated
    }

@sample_bp.route('/sample', methods=['GET'])
def get_post_samples():
    return jsonify([*map(sample_serializer, Sample.query.filter_by(user_id=g.user.id).all())])

@sample_bp.route('/sample', methods=['POST'])
def create_sample():
    data = json.loads(request.data)
    sample = Sample(
        user_id = g.user.id,
        sample_title = data['sample_title']
        )
    sample.initial_data = data['initial_data']
    sample.added_data = []
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
        sample.added_data = data['added_data']
        sample.sample_title = data['sample_title']
        db.session.commit()
        return jsonify({"status": "204", "message": "Successfully updated"})
    # Destroy route
    elif request.method == 'DELETE':
        db.session.delete(sample)
        db.session.commit()
        return jsonify({"status": "204", "message": "Successfully deleted"})