from app import db, admin
from models import User, Image
from flask.ext.admin.contrib.sqlamodel import ModelView

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Image, db.session))