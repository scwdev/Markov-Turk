from datetime import datetime
from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy

from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    ## Todo email validation
    email = db.Column(db.String(50), unique = True, nullable = False)
    ## Todo hash, unique
    api_key = db.Column(db.String(50), nullable = False)
    samples = db.relationship('Sample', backref='user', lazy=True)
    date_created = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return f'{self.id}, {self.email}, {self.api_key}, {self.date_created}'

class Sample(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    data_title = db.Column(db.String(50), nullable = False)
    initial_data = db.Column(db.Text, nullable = False)
    added_data = db.Column(db.Text)
    matrices = db.relationship('Matrix', backref='sample', lazy = True)
    date_created = db.Column(db.DateTime, default=datetime.now)    

    def __repr__(self):
        return f'{self.id}, {self.user_id}, {self.data_title}, {self.date_created}'


class Matrix(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    sample_id = db.Column(db.Integer, db.ForeignKey('sample.id'))
    matrix_title = db.Column(db.String(50), nullable = False)
    matrix = db.Column(db.JSON, nullable = False)
    outputs = db.relationship('Output', backref='matrix', lazy = True)
    date_created = db.Column(db.DateTime, default=datetime.now)    
    
    def __repr__(self):
        return f'{self.id}, {self.sample_id}, {self.matrix_title}, {self.date_created}'


class Output(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    matrix_id = db.Column(db.Integer, db.ForeignKey('matrix.id'))
    generated = db.Column(db.Text, nullable = False)
    date_created = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return f'{self.id}, {self.matrix_id}, {self.date_created}'