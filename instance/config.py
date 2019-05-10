import os


SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-peg-dashboard-key'
SQLALCHEMY_DATABASE_URI = os.environ.get('DB_URI')
