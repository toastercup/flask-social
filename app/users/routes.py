from flask import Blueprint, jsonify, g, session, request
from werkzeug.security import generate_password_hash
from app.users.decorators import requires_login
from app.users.models import User
from app.decorators import expects_json
from app import db

bp = Blueprint('users', __name__, url_prefix='/users')

#TODO: review usefulness of this AND whether this affects things incorrectly
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
    response = jsonify(message='You are now logged in.')

    response.status_code = 200
    return response

@bp.route('/register', methods=['POST'])
@expects_json
def register():
    data = request.json
    user = User(data['username'], generate_password_hash(data['password']))

    db.session.add(user)
    db.session.commit()

    session['user_id'] = user.id

    response = jsonify(message='User has been registered.')

    #TODO: Condense all these repeated HTTP OK messages into a function
    response.status_code = 200
    return response