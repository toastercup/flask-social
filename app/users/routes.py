from flask import Blueprint
from flask import jsonify

bp = Blueprint('users', __name__)

@bp.before_request
def restrict_bp_to_users():
    if False:
        return "buh"

@bp.route('/', methods = ['GET'])
def users():
    data = {
        '1' : 'Bob',
        '2' : 'Katy'
    }

    response = jsonify(data)
    response.status_code = 200

    return response

@bp.route('/<int:userid>', methods = ['GET'])
def user(userid):
    data = {
        'userid'    : userid
    }

    response = jsonify(data)
    response.status_code = 200

    return response
