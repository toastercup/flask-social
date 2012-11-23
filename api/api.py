from flask import Blueprint
from flask import jsonify

bp = Blueprint('api', __name__)

@bp.before_request
def restrict_bp_to_users():
    if False:
        return "buh"

@bp.route('/')
def api_root():
    response = jsonify(message=str('Look inside!'))
    response.status_code = 200
    
    return response

@bp.route('/users', methods = ['GET'])
def api_users():
    data = {
        '1' : 'Bob',
        '2' : 'Katy'
    }

    response = jsonify(data)
    response.status_code = 200

    return response

@bp.route('/users/<int:userid>', methods = ['GET'])
def api_user(userid):
    data = {
        'userid'    : userid
    }

    response = jsonify(data)
    response.status_code = 200

    return response
