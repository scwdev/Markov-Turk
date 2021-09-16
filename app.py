
import os
from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql://scwd:ofekdekel@localhost:5432/markov')

db = SQLAlchemy(app)

migrate = Migrate(app,db)

from controllers.user import user_bp
from controllers.sample import sample_bp
from controllers.matrix import matrix_bp
from controllers.output import output_bp

app.register_blueprint(user_bp)
app.register_blueprint(sample_bp)
app.register_blueprint(matrix_bp)
app.register_blueprint(output_bp)

@app.route('/', methods=['GET'])
def test():
    return '<h1> test </h1>'