from flask import Blueprint, g, request
from flask.ext import restful
from werkzeug.security import generate_password_hash
from app.users.models import User
from app.decorators import AuthResource, JsonResource
from app import db, rest
from sqlalchemy.exc import IntegrityError

class Users(AuthResource):
    def get(self):
        return {
            '1' : 'Bob',
            '2' : 'Katy'
        }

class User(restful.Resource):
    def get(self, user_id):
        return {'user_id' : user_id}

class UserMe(restful.Resource):
    def get(self):
        return_data = {
            'id' : g.user.id,
            'email' : g.user.email,
            'name' : g.user.name,
            'status' : g.user.getStatus(),
            'role' : g.user.getRole()
        }

        return return_data

class UserRegister(JsonResource):
    def post(self):
        request_data = request.json

        user = User(email=request_data['email'], password_hash=generate_password_hash(request_data['password']), name=None)

        db.session.add(user)
        db.session.commit()

        return_data = {
            'message' : 'User has been registered with email address {email}.'.format(email=request_data['email'])
        }

        return return_data

#@rest.handle_error(IntegrityError)
def integrity_error(e):
    return
    return HttpResponse.CONFLICT('User with supplied email address already exists.')