
import os
from flask import Flask, url_for, jsonify
from flask.json import load
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')



CORS(app)

db = SQLAlchemy(app)

migrate = Migrate(app,db)

from controllers.user import user_bp
from controllers.sample import sample_bp
from controllers.matrix import matrix_bp
from controllers.output import output_bp
from controllers.generator import generator_bp

app.register_blueprint(user_bp)
app.register_blueprint(sample_bp)
app.register_blueprint(matrix_bp)
app.register_blueprint(output_bp)
app.register_blueprint(generator_bp)

@app.route('/', methods=['GET'])
def welcom():
    return jsonify({"status": 200, "message": "Welcome!"})