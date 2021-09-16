from itertools import repeat

from flask import jsonify, request, Blueprint, g
from app import db

from controllers.utilities import key_check, n_gram_er, text_generator

generator_bp = Blueprint('generator', __name__, url_prefix='/<api_key>')

@generator_bp.url_value_preprocessor
def handle_key(endpoints, values):
    api_key = values.pop('api_key')
    g.user = key_check(api_key)

@generator_bp.before_request
def check_key():
    if g.user == None:
        return jsonify({'status': 401, 'message': 'No such key.'})

@generator_bp.route('/generate-text/', methods=["POST"])
def generate_text_from_json():
    training_data = request.data['training_data']
    print('\n \n ----- \n \n')
    print(training_data)
    print('\n \n ----- \n \n')
    n = request.args.get('n')
    gram = request.args.get('gram')
    length = request.args.get('length')

    p_matrix = n_gram_er(training_data, n, gram)

    return jsonify({'generated_text': text_generator(p_matrix, gram, length)})



#############################################


#     data = json.loads(request.data)
#     matrix = Matrix.query.get(matrix_id)
#     if matrix.user_id != g.user.id:
#         return jsonify({"status": 400, "message": f'Matrix {matrix_id} does not exist or is not authorized for access by this key'})
#     output = Output(
#         user_id = g.user.id,
#         matrix_id = matrix_id,
#         output_title = data['output_title'],
#         generated = text_generator(matrix.matrix, "word", 100)
#     )
#     db.session.add(output)
#     db.session.commit()

#     return jsonify(output_serializer(output))


# @matrix_bp.route('/sample/<sample_id>/matrix', methods=["POST"])
# def create_matrix(sample_id):
#     data = json.loads(request.data)
#     sample = Sample.query.get(sample_id)
#     if g.user.id != sample.user_id:
#         return jsonify({"status": 400, "message": f'Sample {sample_id} does not exist or is not authorized for access by this key'})
#     matrix = Matrix(
#         sample_id = sample.id,
#         user_id = g.user.id,
#         matrix_title = data["matrix_title"],
#         matrix = n_gram_er(sample.training_data(), data["n"], data["gram"])
#     )
#     # print("\n-----\n")
#     # print(sample.training_data())
#     # print("\n-----\n")
#     db.session.add(matrix)
#     db.session.commit()

# @generator_bp.route('/output/<id>', methods=["GET", "PUT", "DELETE"])
# def single_output(id):
#     id = id
#     return jsonify({'message': 'ding'})