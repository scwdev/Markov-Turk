from flask import jsonify, request, json, Blueprint
from app import db

from models.matrix import Matrix
from controllers.utilities import key_check

matrix_bp = Blueprint('matrix', __name__)

def matrix_serializer(matrix):
    pass

@matrix_bp.route('/matrix/<api_key>', methods=["GET, POST"])
def get_matrices(api_key):
    user = key_check(api_key)
    pass

@matrix_bp.route('/matrix/<api_key>/<id>', methods=["GET, PUT, DELETE"])
def single_matrix(api_key, id):
    user = key_check(api_key)
    pass