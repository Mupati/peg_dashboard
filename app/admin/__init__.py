from flask import Blueprint

admin = Blueprint('admin', '__init__')

from . import views
