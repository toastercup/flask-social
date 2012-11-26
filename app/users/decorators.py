from functools import wraps
from flask import g, request
from werkzeug.security import check_password_hash
from app.users.models import User
from app.helpers import HttpResponse

def requires_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth = request.authorization

        #TODO: Multiple return paths in a decorator...? Not bad practice?
        if not auth:
            return HttpResponse.UNAUTHORIZED()

        user = User.query.filter_by(email=auth.username).first()

        if not (user and check_password_hash(user.password, auth.password)):
            return HttpResponse.UNAUTHORIZED('Authentication Failed.')

        g.user = user
        return f(*args, **kwargs)
    return decorated_function
