from flask.ext.sqlalchemy import SQLAlchemy
from app.utility import make_json_app, HttpResponse
import config

app = make_json_app(__name__)
app.config.from_object(config.DevConfig)

db = SQLAlchemy(app)

@app.errorhandler(301)
def trailing_slash_json(error):
    return HttpResponse.BAD_REQUEST('Please include trailing slash.')

from app.users.routes import bp as usersBp
app.register_blueprint(usersBp)

from app.admin.routes import bp as adminBp
app.register_blueprint(adminBp)
