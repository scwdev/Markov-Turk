from flask import jsonify, request, json, Blueprint
from app import db

from models.output import Output
from controllers.utilities import key_check

output_bp = Blueprint('output', __name__)


def output_serializer(output):
    pass

@output_bp.route('/output/<api_key>', methods=["GET, POST"])
def get_matrices(api_key):
    user = key_check(api_key)
    pass

@output_bp.route('/output/<api_key>/<id>', methods=["GET, PUT, DELETE"])
def single_output(api_key, id):
    user = key_check(api_key)
    pass