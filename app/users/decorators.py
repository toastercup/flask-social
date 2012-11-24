from functools import wraps
from flask import g, jsonify, request, session
from werkzeug.security import check_password_hash
from app.users.models import User

def requires_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth = request.authorization

        if not auth:
            if g.user is None:
                return request_auth()

        elif not check_auth(auth.username, auth.password):
            return request_auth('Authentication Failed.')

        session['user_id'] = user.id
        return f(*args, **kwargs)
    return decorated_function

def request_auth(auth_message="Please Authenticate."):
    message = {'message': auth_message}
    response = jsonify(message)

    response.status_code = 401
    response.headers['WWW-Authenticate'] = 'Basic realm="Example"'

    return response

def check_auth(username, password):
    user = User.query.filter_by(email=username).first()
    return user and check_password_hash(user.password, password)
