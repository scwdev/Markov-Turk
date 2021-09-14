from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://scwd:ofekdekel@localhost:5432/markov'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    ## Todo email validation
    email = db.Column(db.String(50), unique = True, nullable = False)
    ## Todo hash, unique
    api_key = db.Column(db.String(50), nullable = False)
    date_created = db.Column(db.DateTime, default=datetime.now)
    samples = db.relationship('Data_Sample', backref='user', lazy=True)

class Data_Sample(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    data_title = db.Column(db.String(50), nullable = False)
    initial_data = db.Column(db.Text, nullable = False)
    added_data = db.Column(db.Text, nullable = False)
    matrices = db.relationships('Prob_Matrix', backref='')

class Prob_Matrix(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    data_sample_id = db.Column(db.Integer, db.ForeignKey('data_sample.id'))
    matrix_title = db.Column(db.String(50), nullable = False)
    matrix = db.Column(db.JSON, nullable = False)

class Data_Sample(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    prob_matrix_id = db.Column(db.Integer, db.ForeignKey('prob_matrix.id'))
