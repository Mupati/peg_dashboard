from flask_wtf import FlaskForm
from wtforms import FloatField, StringField, SubmitField, SelectField, DateTimeField, FormField, FieldList
from wtforms.validators import DataRequired, InputRequired

from ..models import Product


class ProductForm(FlaskForm):
    """
    form for admin to add new products
    """
    name = StringField(u'Name', validators=[DataRequired()])
    deposit = FloatField(u'Deposit', validators=[DataRequired()])
    total_price = FloatField(u'Total Price', validators=[DataRequired()])
    payment_frequency = StringField(
        u'Payment Frequency', validators=[DataRequired()])
    payment_amount = FloatField(u'Payment Amount', validators=[DataRequired()])
    submit = SubmitField('Add Product')


class CustomerForm(FlaskForm):
    """
    form for admin to add new customers
    """
    first_name = StringField(u'First Name', validators=[DataRequired()])
    last_name = StringField(u'Last Name', validators=[DataRequired()])
    submit = SubmitField('Add Customer')


class ContractForm(FlaskForm):
    """
    form for admin to create new contracts
    """
    customer_id = SelectField(u'Customer Name', validators=[DataRequired()])
    product_id = SelectField(u'Product Name', validators=[DataRequired()])
    submit = SubmitField(u'Create Contract')


class TransactionForm(FlaskForm):
    """
    form for admin initiate new transactions
    """
    status = StringField(u'Status', validators=[DataRequired()])
    type = StringField(u'Type', validators=[DataRequired()])
    amount = FloatField(u'Amount', validators=[DataRequired()])
    # try_contract = FormField(ContractForm)
    contract = SelectField(u'Contract', validators=[DataRequired()])
    submit = SubmitField(u'Create Transaction')
