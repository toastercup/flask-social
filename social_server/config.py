#-----------------------------
# App Configuration


class Config:
    SECRET_KEY = "123456790"

    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.sqlite'
    SQLALCHEMY_ECHO = True

    DEBUG = False


class DevConfig(Config):
    DEBUG = True
