from app import db
from models.mixins import Id_and_Timestamp


class User(Id_and_Timestamp, db.Model):
    email = db.Column(db.String(50), unique = True, nullable = False)
    api_key = db.Column(db.String(50), nullable = False)
    samples = db.relationship('Sample', backref='user', cascade='all, delete', lazy=True)
    matrices = db.relationship('Matrix', backref='user', cascade='all, delete', lazy=True)
    outputs = db.relationship('Output', backref='user', cascade='all, delete', lazy=True)

    def __repr__(self):
        return f'user ID: {self.id}, email: {self.email}, api key: {self.api_key}, created: {self.created}'
