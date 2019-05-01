from flask import render_template
from . import auth


@auth.route('/auth/login')
def index():
    return render_template('auth/login.html')
