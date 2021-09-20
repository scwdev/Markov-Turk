from itertools import repeat

from flask import jsonify, json, request, Blueprint, g

from controllers.utilities import key_check, n_gram_er, text_generator
from models.sample import Sample
from models.matrix import Matrix

generator_bp = Blueprint('generator', __name__, url_prefix='/<api_key>')

@generator_bp.url_value_preprocessor
def handle_key(endpoints, values):
    api_key = values.pop('api_key')
    g.user = key_check(api_key)

@generator_bp.before_request
def check_key():
    if g.user == None:
        return jsonify({'status': 401, 'message': 'No such key.'})


@generator_bp.route('/generate-text', methods=["POST"])
def generate_text_from_json():

    data = json.loads(request.data)

    training_data = data['training_data']
    if sum(map(len,training_data)) > 10000:
        return jsonify({'status': 400, 'message': f'Training-data too long. Please limit to 10,000 characters.'})

    length = data['length']
    if length > 10000:
        return jsonify({'status': 400, 'message': 'Requested text length too long. Please limit to 10,000.'})
    
    n = data['n']
    gram = data['gram']
    
    p_matrix = n_gram_er(training_data, n, gram)

    return jsonify({'generated_text': text_generator(p_matrix, gram, length)})


@generator_bp.route('/generate-text/sample/<id>/<n>/<gram>/<length>', methods=["GET"])
def generate_text_from_sample(id, n, gram, length):

    sample = Sample.query.get(id)
    if sample == None or sample.user_id != g.user.id:
        return jsonify({"status": 400, "message": f'Sample {id} does not exist or is not authorized for access by this key'})

    p_matrix = n_gram_er(sample.training_data(), int(n), gram)

    return jsonify({'generated_text': text_generator(p_matrix, gram, int(length), )})


@generator_bp.route('/generate-text/matrix/<id>/<length>', methods=["GET"])
def generate_text_from_matrix(id, length):

    start = request.args.get("start")
    print(start)
    matrix = Matrix.query.get(id)
    if matrix == None or matrix.user_id != g.user.id:
        return jsonify({"status": 400, "message": f'Matrix {id} does not exist or is not authorized for access by this key'})

    return jsonify({'generated_text': text_generator(matrix.matrix, matrix.gram, int(length), start)})