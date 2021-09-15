from datetime import datetime

from app import db
from models.mixins import Id_and_Timestamp

class Output(Id_and_Timestamp, db.Model):
    # id = db.Column(db.Integer, primary_key = True)
    matrix_id = db.Column(db.Integer, db.ForeignKey('matrix.id'))
    generated = db.Column(db.Text, nullable = False)
    # date_created = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return f'{self.id}, {self.matrix_id}, {self.created}'