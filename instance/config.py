import os


SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-peg-application-key'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://peg_admin:2015ad@localhost/peg_db'
