from flask import json

from app import db
from models.mixins import Id_and_Timestamp, User_Foreign_Key

class Matrix(Id_and_Timestamp, User_Foreign_Key, db.Model):
    sample_id = db.Column(db.Integer, db.ForeignKey('sample.id'))
    matrix_title = db.Column(db.String(50), nullable = False)
    n = db.Column(db.Integer, nullable = False)
    gram = db.Column(db.String(10), nullable = False)
    _matrix = db.Column(db.Text, nullable = False)
    outputs = db.relationship('Output', backref='matrix', cascade='all, delete', lazy = True)
    
    def get_matrix(self):
        return self._matrix
    def set_matrix(self, matrix):
        self._matrix = json.dumps(matrix)

    matrix = property(get_matrix, set_matrix)

    def __repr__(self):
        return f'matrix id: {self.id}, sample_id: {self.sample_id}, title: {self.matrix_title}, created: {self.created}'
