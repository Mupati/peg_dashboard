from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

from ..models import Employee


class RegistrationForm(FlaskForm):
    """
    Form for users to create new account
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    # first_name = StringField('First Name', validators=[DataRequired()])
    # last_name = StringField('Last Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[
        DataRequired(),
        EqualTo('confirm_password')
    ])
    confirm_password = PasswordField('Confirm Password')
    submit = SubmitField('Add Employee')

    def validate_email(self, field):
        if Employee.query.filter_by(email=field.data).first():
            raise ValidationError('Email is already in use.')


class LoginForm(FlaskForm):
    """
    Login Form For Employees and Admins
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log in')


class DepartmentForm(FlaskForm):
    """
    Department Creation/Addition Form
    """
    name = StringField('Name', validators=DataRequired())
    description = StringField('Description', validators=DataRequired())


class RolesForm(FlaskForm):
    """
    Roles for Company Employees
    They are: staff, editor, admin
    """
    name = StringField('Name', validators=DataRequired())
    description = StringField('Description', validators=DataRequired())


class CountryForm(FlaskForm):
    name = StringField('Name', validators=DataRequired())
