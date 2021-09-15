from models.user import User


def key_check(api_key):
    user = User.query.filter_by(api_key=api_key).first()
    return user
