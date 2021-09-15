from datetime import datetime

from app import db
from models.mixins import Id_and_Timestamp


class User(Id_and_Timestamp, db.Model):
    # id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(50), unique = True, nullable = False)
    api_key = db.Column(db.String(50), nullable = False)
    samples = db.relationship('Sample', backref='user', lazy=True)
    # date_created = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return f'{self.id}, {self.email}, {self.api_key}, {self.created}'
