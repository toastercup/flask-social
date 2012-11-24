from flask.ext.sqlalchemy import SQLAlchemy
import utility, config
from app.users.routes import bp as usersBp
from app.admin.routes import bp as adminBp

app = utility.make_json_app(__name__)
app.config.from_object(config.DevConfig)

db = SQLAlchemy(app)

@app.errorhandler(500)
def not_found(error):
    return "No"

app.register_blueprint(usersBp, url_prefix='/users')
app.register_blueprint(adminBp, url_prefix='/admin')
