from flask import render_template, redirect, flash, url_for
from flask_login import login_required, login_user, logout_user

from . import auth
from .forms import LoginForm, RegistrationForm
from .. import db
from ..models import Employee


@auth.route('/auth/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        employee = Employee.query.filter_by(email=form.email.data).first()
        # check password validity
        if employee is not None and employee.verify_password(
                form.password.data):
            # log employee in
            login_user(employee)
            # redirect to the dashboard page after login
            return redirect(url_for('home.index'))
        # when login details are incorrect
        else:
            flash('Invalid Email or Password.')
    return render_template('auth/login.html', title='Log in', form=form)


@auth.route('/auth/register', methods=['GET', 'POST'])
def register():
    """
    Handle registration
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        employee = Employee(email=form.email.data,
                            password=form.password.data)

        # store employee details in db
        db.session.add(employee)
        db.session.commit()
        flash('You have successfully registered! You may now login.')

        # redirect to the login page
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html', title='Register', form=form)


@auth.route('/logout')
@login_required
def logout():
    """
    Logout employee
    """
    logout_user()
    flash('You have successfully been logged out.')

    # redirect to the login page
    return redirect(url_for('auth.login'))
