from flask.ext.admin.contrib.sqlamodel import ModelView

from app import db, admin
from models import Image


admin.add_view(ModelView(Image, db.session))