from flask.ext.sqlalchemy import SQLAlchemy
from flask import jsonify
import app.utility, config

app = app.utility.make_json_app(__name__)
app.config.from_object(config.DevConfig)

db = SQLAlchemy(app)

@app.errorhandler(301)
def trailing_slash_json(error):
    response = jsonify(message='Please include trailing slash.')

    response.status_code = 200
    return response

from app.users.routes import bp as usersBp
app.register_blueprint(usersBp)

from app.admin.routes import bp as adminBp
app.register_blueprint(adminBp)
