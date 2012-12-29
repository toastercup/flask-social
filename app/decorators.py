import httplib
from functools import wraps
from flask import g, request
from flask.ext.restful import abort
from werkzeug.security import check_password_hash
from app.users.models import User

def expects_json(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not 'application/json' in request.headers['Content-Type']:
            abort(httplib.BAD_REQUEST, error='Content-Type is not application/json.')
        return func(*args, **kwargs)

    return wrapper


def requires_auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth_request = request.authorization

        if not auth_request:
            return {'error': 'Please authenticate.'}, httplib.UNAUTHORIZED, {'WWW-Authenticate': 'Basic realm="social"'}

        user = User.query.filter_by(email=auth_request.username).first()

        if not (user and check_password_hash(user.password_hash, auth_request.password)):
            return {'error': 'Authentication failed.'}, httplib.UNAUTHORIZED, {
            'WWW-Authenticate': 'Basic realm="social"'}

        g.user = user
        return func(*args, **kwargs)

    return wrapper
