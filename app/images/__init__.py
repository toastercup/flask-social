from app import db, admin
from models import Image
from flask.ext.admin.contrib.sqlamodel import ModelView

admin.add_view(ModelView(Image, db.session))