from flask import Blueprint, g, request
from werkzeug.security import generate_password_hash
from app.users.models import User
from app.decorators import expects_json, requires_login
from app.helpers import HttpResponse
from app import db
from sqlalchemy.exc import IntegrityError

bp = Blueprint('users', __name__, url_prefix='/users')

@bp.route('/', methods = ['GET'])
@requires_login
def users():
    return_data = {
        '1' : 'Bob',
        '2' : 'Katy'
    }

    response = HttpResponse.OK(return_data)
    return response

@bp.route('/<int:userid>', methods = ['GET'])
@requires_login
def user(userid):
    return_data = {
        'userid' : userid
    }

    response = HttpResponse.OK(return_data)
    return response

@bp.route('/me', methods = ['GET'])
@requires_login
def me():
    return_data = {
        'id' : g.user.id,
        'email' : g.user.email,
        'name' : g.user.name,
        'status' : g.user.getStatus(),
        'role' : g.user.getRole()
    }

    response = HttpResponse.OK(return_data)
    return response

@bp.route('/register', methods=['POST'])
@expects_json
def register():
    request_data = request.json

    user = User(email=request_data['email'], password_hash=generate_password_hash(request_data['password']), name=None)

    db.session.add(user)
    db.session.commit()

    return_data = {
        'message' : 'User has been registered with email address {email}.'.format(email=request_data['email'])
    }

    response = HttpResponse.OK(return_data)
    return response

@bp.errorhandler(IntegrityError)
def integrity_error(e):
    return HttpResponse.CONFLICT('User with supplied email address already exists.')