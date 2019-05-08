from flask_wtf import FlaskForm
from wtforms import FloatField, StringField, SubmitField, SelectField, DateTimeField, FormField, FieldList
from wtforms.validators import DataRequired

from ..models import Product


class ProductForm(FlaskForm):
    """
    form for admin to add new products
    """
    name = StringField(u'name')
    deposit = FloatField(u'deposit')
    total_price = FloatField(u'total price')
    payment_frequency = StringField(u'payment frequency')
    payment_amount = FloatField(u'payment amount')
    submit = SubmitField('send')


class CustomerForm(FlaskForm):
    """
    form for admin to add new customers
    """
    first_name = StringField(u'first_name')
    last_name = StringField(u'last_name')
    submit = SubmitField('send')


class ContractForm(FlaskForm):
    """
    form for admin to create new contracts
    """
    customer_id = SelectField(u'customer')
    product_id = SelectField(u'product')
    submit = SubmitField(u'send')


class TransactionForm(FlaskForm):
    """
    form for admin initiate new transactions
    """
    status = StringField(u'status')
    type = StringField(u'type')
    amount = FloatField(u'amount')
    try_contract = FormField(ContractForm)
    submit = SubmitField(u'create')
