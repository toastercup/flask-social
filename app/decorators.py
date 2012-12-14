import httplib
from functools import wraps
from flask import g, request, make_response, current_app
from flask.ext.restful import abort
from werkzeug.security import check_password_hash
from app.users.models import User
from datetime import timedelta
from functools import update_wrapper

def expects_json(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if request.headers['Content-Type'] != 'application/json':
            abort(httplib.BAD_REQUEST, error='Data must be in JSON format.')
        return func(*args, **kwargs)
    return wrapper

def requires_auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth_request = request.authorization

        if not auth_request:
            return {'error' : 'Please authenticate.'}, httplib.UNAUTHORIZED, {'WWW-Authenticate' : 'Basic realm="social"'}

        user = User.query.filter_by(email=auth_request.username).first()

        if not (user and check_password_hash(user.password_hash, auth_request.password)):
            return {'error' : 'Authentication failed.'}, httplib.UNAUTHORIZED, {'WWW-Authenticate' : 'Basic realm="social"'}

        g.user = user
        return func(*args, **kwargs)
    return wrapper


def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator