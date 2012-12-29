from datetime import datetime

from app import db
from flask.ext.sqlalchemy import BaseQuery
from werkzeug.security import check_password_hash
import constants as USER


class UserQuery(BaseQuery):
    def authenticate(self, email, password):
        user = self.filter(User.email==email).first()
        if user:
            authenticated = user.check_password(password)
        else:
            authenticated = False

        return user, authenticated


class User(db.Model):
    query_class = UserQuery

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    password_hash = db.Column(db.String(80))
    name = db.Column(db.String(50))
    description = db.Column(db.Text)
    updated = db.Column(db.DateTime)
    role = db.Column(db.SmallInteger, default=USER.USER)
    status = db.Column(db.SmallInteger, default=USER.NEW)

    def __init__(self, email, password_hash, name, description=None):
        self.email = email
        self.password_hash = password_hash
        self.name = name
        self.description = description
        self.updated = datetime.utcnow()

    def getStatus(self):
        return USER.STATUS[self.status]

    def getRole(self):
        return USER.ROLE[self.role]

    def check_password(self, password):
        if self.password_hash is None:
            return False
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<%s>' % (self)

    def __str__(self):
        return self.name