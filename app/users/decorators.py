from functools import wraps
from flask import g, jsonify, request, session
from werkzeug.security import check_password_hash
from app.users.models import User
from app.utility import HttpResponse

def requires_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth = request.authorization

        if not auth:
            return request_auth()

        user = User.query.filter_by(email=auth.username).first()

        if not (user and check_password_hash(user.password, auth.password)):
            return request_auth('Authentication Failed.')

        g.user = user
        return f(*args, **kwargs)
    return decorated_function

def request_auth(auth_message="Please Authenticate."):
    response = HttpResponse.UNAUTHORIZED(auth_message)

    return response
