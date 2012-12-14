import httplib, fields
from flask import g, request
from flask.ext.restful import Resource, abort, marshal_with
from werkzeug.security import generate_password_hash
from app.users.models import User
from app.decorators import requires_auth, expects_json, crossdomain
from app import db
from sqlalchemy.exc import IntegrityError
from validation import RegisterForm
from simples3 import S3Bucket

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
                'role' : user.getRole(),
                'description' : user.description,
                'updated' : user.updated
            }

        return usersDict

class UserResource(Resource):
    @requires_auth
    @marshal_with(fields.user_fields)
    def get(self, user_id):
        user = User.query.filter_by(id=user_id).first()

        return user

class UserMeResource(Resource):
    @requires_auth
    @marshal_with(fields.user_fields)
    def get(self):
        return g.user

class UserRegisterResource(Resource):
    @expects_json
    @crossdomain(origin='*')
    def post(self):
        form = RegisterForm.from_json(request.json)

        if form.validate():
            user = User(email=form.data['email'], password_hash=generate_password_hash(form.data['password']), name=form.data['name'], description=form.data['description'])

            db.session.add(user)

            try:
                db.session.commit()
            except IntegrityError as error:
                abort(httplib.CONFLICT, error='User with supplied email address already exists.')

            return {'message' : 'User has been registered with email address {email}.'.format(email=form.data['email'])}
        else:
            abort(httplib.NOT_ACCEPTABLE, errors=form.errors)