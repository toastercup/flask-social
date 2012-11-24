from functools import wraps
from flask import g, jsonify

def requires_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            response = jsonify(message=str('Not authorized. Please login.'))
            response.status_code = 401
            return response
        return f(*args, **kwargs)
    return decorated_function