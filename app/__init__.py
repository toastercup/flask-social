from flask.ext.sqlalchemy import SQLAlchemy
import utility, config
from app.users.routes import bp as usersBp
from app.admin.routes import bp as adminBp

app = utility.make_json_app(__name__)
app.config.from_object(config.DevConfig)

db = SQLAlchemy(app)

@app.errorhandler(301)
def not_found(error):
    return "No"

app.register_blueprint(usersBp)
app.register_blueprint(adminBp)
