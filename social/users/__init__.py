from flask.ext.admin.contrib.sqlamodel import ModelView

from social import db, admin
from social.users.models import User


admin.add_view(ModelView(User, db.session))
