import httplib
from flask import g, request
from flask.ext.restful import Resource, abort
from werkzeug.security import generate_password_hash
from app.users.models import User
from app.decorators import requires_auth, expects_json
from app import db
from sqlalchemy.exc import IntegrityError

class UsersResource(Resource):
    @requires_auth
    def get(self):
        return {
            '1' : 'Bob',
            '2' : 'Katy'
        }

class UserResource(Resource):
    @requires_auth
    def get(self, user_id):
        return {'user_id' : user_id}

class UserMeResource(Resource):
    @requires_auth
    def get(self):
        return_data = {
            'id' : g.user.id,
            'email' : g.user.email,
            'name' : g.user.name,
            'status' : g.user.getStatus(),
            'role' : g.user.getRole()
        }

        return return_data

class UserRegisterResource(Resource):
    @expects_json
    def post(self):
        request_data = request.json

        user = User(email=request_data['email'], password_hash=generate_password_hash(request_data['password']), name=request_data['name'])

        db.session.add(user)

        try:
            db.session.commit()
        except IntegrityError as e:
            abort(httplib.CONFLICT, message='User with supplied email address already exists.')

        return {'message' : 'User has been registered with email address {email}.'.format(email=request_data['email'])}