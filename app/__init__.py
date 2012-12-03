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

@app.errorhandler(301)
def trailing_slash_json(error):
    return HttpResponse.BAD_REQUEST('Please include trailing slash.')

from app.users.routes import bp as usersBp
app.register_blueprint(usersBp)
