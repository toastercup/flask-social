from app import db
from datetime import datetime
import constants as USER

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    password_hash = db.Column(db.String(80))
    name = db.Column(db.String(50))
    description = db.Column(db.Text)
    updated = db.Column(db.DateTime)
    role = db.Column(db.SmallInteger, default=USER.USER)
    status = db.Column(db.SmallInteger, default=USER.NEW)

    def __init__(self, email, password_hash, name):
        self.email = email
        self.password_hash = password_hash
        self.name = name
        self.updated = datetime.utcnow()

    def getStatus(self):
        return USER.STATUS[self.status]

    def getRole(self):
        return USER.ROLE[self.role]

    def __repr__(self):
        return '<User %r>' % (self.name)
