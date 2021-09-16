from datetime import datetime
from sqlalchemy.ext.declarative import declared_attr

from app import db

class Id_and_Timestamp(object):
    id = db.Column(db.Integer, primary_key = True)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated = db.Column(db.DateTime, onupdate=datetime.utcnow)

class User_Foreign_Key(object):
    @declared_attr
    def user_id(cls):
        return db.Column(db.Integer, db.ForeignKey('user.id'))