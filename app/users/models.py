from app import db, admin
from app.users import constants as USER
from flask.ext.admin.contrib.sqlamodel import ModelView

class User(db.Model):
    __tablename__ = 'users_user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    name = db.Column(db.String(50))
    password_hash = db.Column(db.String(80))
    role = db.Column(db.SmallInteger, default=USER.USER)
    status = db.Column(db.SmallInteger, default=USER.NEW)

    def __init__(self, email, password_hash, name=None):
        self.email = email
        self.password_hash = password_hash
        self.name = name

    def getStatus(self):
        return USER.STATUS[self.status]

    def getRole(self):
        return USER.ROLE[self.role]

    def __repr__(self):
        return '<User %r>' % (self.name)

admin.add_view(ModelView(User, db.session))