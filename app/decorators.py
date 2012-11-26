from functools import wraps
from flask import jsonify, request
from app.helpers import HttpResponse

def expects_json(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.headers['Content-Type'] != 'application/json':
            return HttpResponse.BAD_REQUEST('Data must be in JSON format.')
        return f(*args, **kwargs)
    return decorated_function