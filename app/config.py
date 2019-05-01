import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-peg-application-key'
    SQLALCHEMY_DATABASE_URI = 'mysql://peg_admin:2015ad@localhost/peg_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
