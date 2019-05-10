from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from app.config import app_config

db = SQLAlchemy()


def create_app(config_name):
    if os.getenv('FLASK_CONFIG') == "production":
        app = Flask(__name__)
        app.config.update(
            SECRET_KEY=os.getenv('SECRET_KEY'),
            SQLALCHEMY_DATABASE_URI=os.getenv('SQLALCHEMY_DATABASE_URI')
        )
    else:
        app = Flask(__name__, instance_relative_config=True)
        app.config.from_object(app_config[config_name])
        app.config.from_pyfile('config.py')

    db.init_app(app)
    migrate = Migrate(app, db, compare_type=True)

    from app import models

    # from .auth import auth as auth_blueprint
    # app.register_blueprint(auth_blueprint)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    return app


# def create_app(config_name):
#     if os.getenv('FLASK_CONFIG') == "production":
#         app = Flask(__name__)
#         app.config.update(
#             SECRET_KEY=os.getenv('SECRET_KEY'),
#             SQLALCHEMY_DATABASE_URI=os.getenv('SQLALCHEMY_DATABASE_URI')
#         )
#     else:
#         app = Flask(__name__, instance_relative_config=True)
#         app.config.from_object(app_config[config_name])
#         app.config.from_pyfile('config.py')
