import httplib
from flask import g, request, jsonify
from flask.ext.restful import Resource, abort
from werkzeug.security import generate_password_hash
from app.users.models import User
from app.decorators import requires_auth, expects_json
from app import db
from sqlalchemy.exc import IntegrityError

class UsersResource(Resource):
    @requires_auth
    def get(self):
        users = User.query.all()

        usersDict = {}
        for user in users:
             usersDict[user.id] = {
                'email' : user.email,
                'name' : user.name,
                'status' : user.getStatus(),
                'role' : user.getRole()
            }

        return usersDict

class UserResource(Resource):
    @requires_auth
    def get(self, user_id):
        user = User.query.filter_by(id=user_id).first()

        return {
            'id' : user_id,
            'email' : user.email,
            'name' : user.name,
            'status' : user.getStatus(),
            'role' : user.getRole()
        }

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