import utility
from api import api
from admin import admin

app = utility.make_json_app(__name__)

app.register_blueprint(api.bp, url_prefix='/api')
app.register_blueprint(admin.bp, url_prefix='/admin')

if __name__ == '__main__':
    app.run(debug=True)
