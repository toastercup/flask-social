from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.admin import Admin
from flask.ext import restful
from flask import Flask
import config, wtforms_json
from decorators import crossdomain

app = Flask(__name__)
app.config.from_object(config.HerokuConfig)

db = SQLAlchemy(app)
admin = Admin(app)
rest = restful.Api(app, prefix='/', default_mediatype='application/json', decorators=crossdomain(origin='*'))

wtforms_json.init()

from app.users.resources import UsersResource, UserResource, UserMeResource, UserRegisterResource
rest.add_resource(UsersResource, '/users/')
rest.add_resource(UserResource, '/users/<int:user_id>/')
rest.add_resource(UserMeResource, '/users/me/')
rest.add_resource(UserRegisterResource, '/users/register/')

from app.images.resources import ImagesResource, ImageResource
rest.add_resource(ImagesResource, '/images/')
rest.add_resource(ImageResource, '/image/')