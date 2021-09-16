from flask import json

from app import db
from models.mixins import Id_and_Timestamp, User_Foreign_Key

class Output(Id_and_Timestamp, User_Foreign_Key,db.Model):
    matrix_id = db.Column(db.Integer, db.ForeignKey('matrix.id'))
    output_title = db.Column(db.String(50), nullable = False)
    _generated = db.Column(db.Text, nullable = False)

    def get_generated(self):
        return json.loads(self._generated)
    def set_generated(self, gen_str):
        self._generated = json.dumps(gen_str)
    
    generated = property(get_generated, set_generated)

    def __repr__(self):
        return f'output id: {self.id}, output title: {self.output_title} matrix id: {self.matrix_id}, created: {self.created}'