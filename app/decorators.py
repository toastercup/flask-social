from functools import wraps
from flask import jsonify, request

def expects_json(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.headers['Content-Type'] != 'application/json':
            message = {'message': 'Data must be in JSON format.'}
            response = jsonify(message)

            response.status_code = 400
            return response
        return f(*args, **kwargs)
    return decorated_function