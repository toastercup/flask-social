from app import db
from app.users import constants as USER

class User(db.Model):
    __tablename__ = 'users_user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(20))
    role = db.Column(db.SmallInteger, default=USER.USER)
    status = db.Column(db.SmallInteger, default=USER.NEW)

    def __init__(self, email=None, name=None, password=None):
        self.email = email
        self.name = name
        self.password = password

    def getStatus(self):
        return USER.STATUS[self.status]

    def getRole(self):
        return USER.ROLE[self.role]

    def __repr__(self):
        return '<User %r>' % (self.name)
