
from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://scwd:ofekdekel@localhost:5432/markov'

db = SQLAlchemy(app)

migrate = Migrate(app,db)

from views.user import user

app.register_blueprint(user)


# class Test(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     ## email validation, unique
#     username = db.Column(db.String(50))
#     ## hash, unique
#     api_key = db.Column(db.String(50))
#     date_created = db.Column(db.DateTime, default=datetime.now)

# # @app.route('/<username>/<api_key>')
# # def index(username, api_key):
# #     test = Test(username=username, api_key=api_key)
# #     db.session.add(test)
# #     db.session.commit()

# #     return '<h1> added new test <h1>'

@app.route('/', methods=['GET'])
def test():
    return '<h1> test </h1>'