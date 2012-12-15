from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.admin import Admin
from flask.ext import restful
from flask import Flask
import config, wtforms_json

app = Flask(__name__)
app.config.from_object(config.HerokuConfig)

db = SQLAlchemy(app)
admin = Admin(app)
rest = restful.Api(app=app, default_mediatype='application/json')

wtforms_json.init()

from app.users.resources import UsersResource, UserResource, UserMeResource, UserRegisterResource
rest.add_resource(UsersResource,
    '/users',
    '/users/')
rest.add_resource(UserResource,
    '/users/<int:user_id>',
    '/users/<int:user_id>/')
rest.add_resource(UserMeResource,
    '/users/me',
    '/users/me/')
rest.add_resource(UserRegisterResource,
    '/users/register'
    '/users/register/')

from app.images.resources import ImagesResource, ImageResource
rest.add_resource(ImagesResource,
    '/images',
    '/images/')
rest.add_resource(ImageResource,
    '/images/<int:image_id>'
    '/images/<int:image_id>/')

@app.after_request
def allow_cors(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Credentials'] = 'true'

    return response