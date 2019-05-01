from flask import render_template
from app import create_app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='HOME')


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('auth/login.html', title='LOGIN')


@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('auth/register.html', title='REGISTER')


# pass the user id and use to populate the content
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard/index.html', title='DASHBOARD')
