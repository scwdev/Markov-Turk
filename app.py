from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://scwd:ofekdekel@localhost:5432/markov'

db = SQLAlchemy(app)

class Test(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    ## Todo email validation, unique
    username = db.Column(db.String(50))
    ## Todo hash, unique
    api_key = db.Column(db.String(50))
    date_created = db.Column(db.DateTime, default=datetime.now)

@app.route('/<username>/<api_key>')
def index(username, api_key):
    test = Test(username=username, api_key=api_key)
    db.session.add(test)
    db.session.commit()

    return '<h1> added new test <h1>'

