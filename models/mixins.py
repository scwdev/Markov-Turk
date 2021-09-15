from datetime import datetime

from app import db

class Id_and_Timestamp(object):
    id = db.Column(db.Integer, primary_key = True)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated = db.Column(db.DateTime, onupdate=datetime.utcnow)