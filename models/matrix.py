from datetime import datetime

from app import db
from models.mixins import Id_and_Timestamp

class Matrix(Id_and_Timestamp, db.Model):
    # id = db.Column(db.Integer, primary_key = True)
    sample_id = db.Column(db.Integer, db.ForeignKey('sample.id'))
    matrix_title = db.Column(db.String(50), nullable = False)
    matrix = db.Column(db.JSON, nullable = False)
    outputs = db.relationship('Output', backref='matrix', lazy = True)
    # date_created = db.Column(db.DateTime, default=datetime.now)    
    
    def __repr__(self):
        return f'{self.id}, {self.sample_id}, {self.matrix_title}, {self.created}'
