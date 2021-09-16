from flask import jsonify, request, json, Blueprint, g
from app import db

from models.output import Output
from models.matrix import Matrix
from controllers.utilities import key_check, text_generator

output_bp = Blueprint('output', __name__, url_prefix='/<api_key>')

@output_bp.url_value_preprocessor
def initial_key_check(endpoints, values):
    api_key = values.pop('api_key')
    g.user = key_check(api_key)
    if g.user == None:
        return jsonify({'status': 401, 'message': 'No such key.'})


def output_serializer(output):
    return {
        "id": output.id,
        "user_id": output.user_id,
        "matrix_id": output.matrix_id,
        "output_title": output.output_title,
        "generated": output.generated,
        "created": output.created,
        "udpated": output.updated
    }

@output_bp.route('/output', methods=["GET"])
def index_outputs():
    return jsonify([*map(output_serializer, Output.query.all())])

@output_bp.route('/matrix/<matrix_id>/output', methods=["POST"])
def create_output(matrix_id):
    data = json.loads(request.data)
    matrix = Matrix.query.get(matrix_id)
    if matrix.user_id != g.user.id:
        return jsonify({"status": 400, "message": f'Matrix {matrix_id} does not exist or is not authorized for access by this key'})
    output = Output(
        user_id = g.user.id,
        matrix_id = matrix_id,
        output_title = data['output_title'],
        generated = text_generator(matrix.matrix, "word", 100)
    )
    db.session.add(output)
    db.session.commit()

    return jsonify(output_serializer(output))

@output_bp.route('/output/<id>', methods=["GET, PUT, DELETE"])
def single_output(api_key, id):
    
    pass