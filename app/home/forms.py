from flask_wtf import FlaskForm
from wtforms import FloatField, StringField, SubmitField, SelectField, DateTimeField, FormField, FieldList
from wtforms.validators import DataRequired

from ..models import Product


class ProductForm(FlaskForm):
    """
    form for admin to add new products
    """
    name = StringField(u'Name')
    deposit = FloatField(u'Deposit')
    total_price = FloatField(u'Total Price')
    payment_frequency = StringField(u'Payment Frequency')
    payment_amount = FloatField(u'Payment Amount')
    submit = SubmitField('Add Product')


class CustomerForm(FlaskForm):
    """
    form for admin to add new customers
    """
    first_name = StringField(u'First Name')
    last_name = StringField(u'Last Name')
    submit = SubmitField('Add Customer')


class ContractForm(FlaskForm):
    """
    form for admin to create new contracts
    """
    customer_id = SelectField(u'Customer Name')
    product_id = SelectField(u'Product Name')
    submit = SubmitField(u'Create Contract')


class TransactionForm(FlaskForm):
    """
    form for admin initiate new transactions
    """
    status = StringField(u'Status')
    type = StringField(u'Type')
    amount = FloatField(u'Amount')
    try_contract = FormField(ContractForm)
    submit = SubmitField(u'Create Transaction')
