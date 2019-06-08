from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from app.config import app_config
from .errors import Errors

db = SQLAlchemy()
login_manager = LoginManager()


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

    login_manager.init_app(app)
    login_manager.login_message = "Access Denied!, You are not Authenticated"
    login_manager.login_view = "auth.login"

    db.init_app(app)
    migrate = Migrate(app, db, compare_type=True)

    from app import models

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    app.register_error_handler(404, Errors.page_not_found)
    app.register_error_handler(403, Errors.forbidden)
    app.register_error_handler(500, Errors.internal_server_error)

    return app
