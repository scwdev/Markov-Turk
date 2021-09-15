from datetime import datetime

from app import db
from models.mixins import Id_and_Timestamp

class Sample(Id_and_Timestamp, db.Model):
    # id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    data_title = db.Column(db.String(50), nullable = False)
    initial_data = db.Column(db.Text, nullable = False)
    added_data = db.Column(db.Text)
    matrices = db.relationship('Matrix', backref='sample', lazy = True)
    # date_created = db.Column(db.DateTime, default=datetime.now)    

    def __repr__(self):
        return f'{self.id}, {self.user_id}, {self.data_title}, {self.created}'