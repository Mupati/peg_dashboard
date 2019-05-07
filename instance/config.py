import os


SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-peg-application-key'
SQLALCHEMY_DATABASE_URI = os.environ.get('DB_URI')
SQLALCHEMY_ECHO = False