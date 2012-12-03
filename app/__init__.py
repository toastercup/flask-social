from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.admin import Admin
from flask.ext import restful
from flask import Flask
import config

app = Flask(__name__)
app.config.from_object(config.DevConfig)

db = SQLAlchemy(app)
admin = Admin(app)
rest = restful.Api(app)

from app.users.resources import UsersResource, UserResource, UserMeResource, UserRegisterResource
rest.add_resource(UsersResource, '/users/')
rest.add_resource(UserResource, '/users/<int:user_id>')
rest.add_resource(UserMeResource, '/users/me')
rest.add_resource(UserRegisterResource, '/users/register')