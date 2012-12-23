from flask.ext.admin.contrib.sqlamodel import ModelView

from app import db, admin
from models import User


admin.add_view(ModelView(User, db.session))