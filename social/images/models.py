from datetime import datetime

from social import db
from social.users.models import User


class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cdn_guid = db.Column(db.String(80), unique=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(80))
    updated = db.Column(db.DateTime)

    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    user = db.relationship(User, backref='images')

    def __init__(self, cdn_guid, title, description):
        self.cdn_guid = cdn_guid
        self.title = title
        self.description = description
        self.updated = datetime.utcnow()

    def __repr__(self):
        return '<cdn_guid %r>' % (self.cdn_guid)
