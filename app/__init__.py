from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.admin import Admin
from flask.ext import restful
from app.helpers import make_json_app, HttpResponse
import config

app = make_json_app(__name__)
app.config.from_object(config.DevConfig)

db = SQLAlchemy(app)
admin = Admin(app)
rest = restful.Api(app)

from app.users.routes import Users, User, UserMe, UserRegister
rest.add_resource(Users, '/users')
rest.add_resource(User, '/users/<int:user_id>')
rest.add_resource(UserMe, '/users/me')
rest.add_resource(UserRegister, '/users/register')
