from flask import json

from app import db
from models.mixins import Id_and_Timestamp, User_Foreign_Key

class Sample(Id_and_Timestamp, User_Foreign_Key, db.Model):
    sample_title = db.Column(db.String(50), nullable = False)
    _initial_data = db.Column(db.Text, nullable = False)
    _added_data = db.Column(db.Text)
    matrices = db.relationship('Matrix', backref='sample', cascade='all, delete' ,lazy = True)

    def get_initial_data(self):
        return json.loads(self._initial_data)
    def set_initial_data(self, data_dict):
        self._initial_data = json.dumps(data_dict)    
    
    initial_data = property(get_initial_data, set_initial_data)

    def get_added_data(self):
        return json.loads(self._added_data)
    def set_added_data(self, data_dict):
        self._added_data = json.dumps(data_dict)
    
    added_data = property(get_added_data, set_added_data)
    
    def training_data(self):
        initial = json.loads(self._initial_data)
        added = json.loads(self._added_data)
        return initial + added

    def __repr__(self):
        return f'sample id: {self.id}, user id: {self.user_id}, title: {self.sample_title}, created: {self.created}'