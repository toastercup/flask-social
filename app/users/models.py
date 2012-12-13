from app import db
from datetime import datetime
from app.users import constants as USER

class User(db.Model):
    __tablename__ = 'users_user'
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


class Image(db.Model):
    __tablename__ = 'images_image'
    id = db.Column(db.Integer, primary_key=True)
    cdn_guid = db.Column(db.String(80), unique=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(80))
    updated = db.Column(db.DateTime)

    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    user = db.relationship(User, backref='images')

    def __init__(self, cdn_guid, title, description):
        self.cdn_guid = cdn_guid
        self.title = title
        self.description = description
        self.updated = datetime.utcnow()

    def __repr__(self):
        return '<cdn_guid %r>' % (self.cdn_guid)