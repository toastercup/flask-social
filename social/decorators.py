import http.client

from functools import wraps
from flask import g, request
from flask.ext.restful import abort

from social.users.models import User

def expects_json(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not 'application/json' in request.headers['Content-Type']:
            abort(http.client.BAD_REQUEST, error='Content-Type is not application/json.')
        return func(*args, **kwargs)

    return wrapper


def requires_auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth_request = request.authorization

        if not auth_request:
            return {'error': 'Please authenticate.'}, http.client.UNAUTHORIZED, {'WWW-Authenticate': 'Basic realm="social"'}

        user, authenticated = User.query.authenticate(auth_request.username, auth_request.password)

        if not authenticated:
            return {'error': 'Authentication failed.'}, http.client.UNAUTHORIZED, {
            'WWW-Authenticate': 'Basic realm="social"'}

        g.user = user
        return func(*args, **kwargs)

    return wrapper
