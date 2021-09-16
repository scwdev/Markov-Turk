from flask import jsonify, request, json, Blueprint, g
from app import db

from models.matrix import Matrix
from models.sample import Sample

from controllers.user import output_serializer
from controllers.utilities import key_check, n_gram_er

matrix_bp = Blueprint('matrix', __name__, url_prefix='/<api_key>')

@matrix_bp.url_value_preprocessor
def initial_key_check(endpoints, values):
    api_key = values.pop('api_key')
    g.user = key_check(api_key)
    if g.user == None:
        return jsonify({'status': 401, 'message': 'No such key.'})

def matrix_serializer(matrix):
    return {
        'user_id': matrix.user_id,
        'id': matrix.id,
        'sample_id': matrix.sample_id,
        'matrix_title': matrix.matrix_title,
        'matrix': matrix.matrix,
        'outputs': [*map(output_serializer, matrix.outputs)],
        'created': matrix.created,
        'updated': matrix.updated
    }

@matrix_bp.route('/matrix', methods=["GET"])
def get_matrices():
    return jsonify([*map(matrix_serializer, Matrix.query.all())])

@matrix_bp.route('/sample/<sample_id>/matrix', methods=["POST"])
def create_matrix(sample_id):
    data = json.loads(request.data)
    sample = Sample.query.get(sample_id)
    matrix = Matrix(
        sample_id = sample.id,
        user_id = g.user.id,
        matrix_title = data["matrix_title"],
        matrix = n_gram_er(sample.initial_data, data["n"], data["gram"])
    )
    db.session.add(matrix)
    db.session.commit()

    return jsonify(matrix_serializer(matrix))
    # return jsonify({"number": 200})

@matrix_bp.route('/matrix/<sample_id>/<matrix_id>', methods=["PUT"])
def update_matrix(sample_id, matrix_id):
    data = json.loads(request.data)
    sample = Sample.query.get(sample_id)
    matrix = Matrix.query.get(matrix_id)
    pass

@matrix_bp.route('/matrix/<matrix_id>', methods=["GET", "DELETE"])
def single_matrix(matrix_id):
    data = json.loads(request.data)
    matrix = Matrix.query.get(matrix_id)
    pass