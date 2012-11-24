import utility, app_config
from api import api
from admin import admin

app = utility.make_json_app(__name__)
app.config.from_object(app_config.DevConfig)

app.register_blueprint(api.bp, url_prefix='/api')
app.register_blueprint(admin.bp, url_prefix='/admin')

if __name__ == '__main__':
    app.run()
