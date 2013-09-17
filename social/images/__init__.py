from flask.ext.admin.contrib.sqlamodel import ModelView

from social import db, admin
from social.images.models import Image


admin.add_view(ModelView(Image, db.session))
