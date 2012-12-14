from app import db, admin
from models import User
from flask.ext.admin.contrib.sqlamodel import ModelView

admin.add_view(ModelView(User, db.session))