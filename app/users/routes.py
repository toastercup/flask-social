from flask import Blueprint, jsonify, g, session
from app.users.decorators import requires_login
from app.users.models import User

bp = Blueprint('users', __name__, url_prefix='/users')

@bp.before_request
def retrieve_user():
    g.user = None
    if 'user_id' in session:
        g.user = User.query.get(session['user_id']);

@bp.route('/', methods = ['GET'])
@requires_login
def users():
    data = {
        '1' : 'Bob',
        '2' : 'Katy'
    }

    response = jsonify(data)
    response.status_code = 200

    return response

@bp.route('/<int:userid>', methods = ['GET'])
@requires_login
def user(userid):
    data = {
        'userid' : userid
    }

    response = jsonify(data)
    response.status_code = 200

    return response

@bp.route('/me', methods = ['GET'])
@requires_login
def me():
    data = {
        'about' : 'hi'
    }

    response = jsonify(data)
    response.status_code = 200

    return response

@bp.route('/login', methods=['POST'])
@requires_login
def login():
    return "You are now logged in."

@bp.route('/register', methods=['POST'])
def register():
    return "Nope"