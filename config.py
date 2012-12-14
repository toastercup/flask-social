import os
_basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = "123456790"

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.db')
    DATABASE_CONNECT_OPTIONS = {}

    RESOURCE_DIR = 'resource'

    ALLOWED_PHOTO_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True


class HerokuConfig(DevConfig):
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']