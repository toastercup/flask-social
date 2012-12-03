import httplib
from functools import wraps
from flask import g, request, jsonify
from flask.ext import restful
from werkzeug.security import check_password_hash
from app.helpers import HttpResponse
from app.users.models import User

def expects_json(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if request.headers['Content-Type'] != 'application/json':
            return "Data must be in JSON format.", httplib.BAD_REQUEST
        return func(*args, **kwargs)
    return wrapper

def requires_auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth_request = request.authorization

        if not auth_request:
            return unauthorized

        user = User.query.filter_by(email=auth_request.username).first()

        if not (user and check_password_hash(user.password_hash, auth_request.password)):
            return "Authentication failed.", httplib.UNAUTHORIZED

        g.user = user
        return func(*args, **kwargs)
    return wrapper

class AuthResource(restful.Resource):
    method_decorators = [requires_auth]

class JsonResource(restful.Resource):
    method_decorators = [expects_json]

def unauthorized(body_message='Please authenticate.'):
    message = {'message': body_message}
    response = jsonify(message)

    response.status_code = httplib.UNAUTHORIZED
    response = restful.unauthorized(response, "user")

    return response