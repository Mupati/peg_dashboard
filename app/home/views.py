from flask import render_template, jsonify, flash, redirect, url_for
from . import home
from .forms import ProductForm, CustomerForm, ContractForm, TransactionForm
from .. import db
from ..models import Product, Customer, Contract, Transaction


@home.route('/index')
@home.route('/')
def index():
    return render_template('home/index.html', title='Dashboard')


@home.route('/customers', methods=['GET', 'POST'])
def customers():
    """
    Render the customer table and
    Add products to the customer table from here
    """
    form = CustomerForm()
    if form.validate_on_submit():
        customer = Customer(first_name=form.first_name.data,
                            last_name=form.last_name.data)
        db.session.add(customer)
        db.session.commit()
        flash('customer successfully added')
        return redirect(url_for('home.index'))
    return render_template('home/customers.html', form=form, title='Customer')


@home.route('/products', methods=['GET', 'POST'])
def products():
    """
    Render the product table and 
    Add products to the products table from here
    """
    form = ProductForm()
    if form.validate_on_submit():
        product = Product(
            name=form.name.data,
            deposit=form.deposit.data,
            total_price=form.total_price.data,
            payment_frequency=form.payment_frequency.data,
            payment_amount=form.payment_amount.data
        )
        db.session.add(product)
        db.session.commit()
        flash('product successfully added')
        return redirect(url_for('home.index'))
    return render_template('home/products.html', form=form, title='Product')


@home.route('/product_data')
def get_product_data():
    # Assume data comes from somewhere else
    data = {
        "data": [
            {
                "id": "1",
                "name": "John Q Public",
                "position": "System Architect",
                "salary": "$320,800",
                "start_date": "2011/04/25",
                "office": "Edinburgh",
                "extn": "5421"
            },
            {
                "id": "2",
                "name": "Larry Bird",
                "position": "Accountant",
                "salary": "$170,750",
                "start_date": "2011/07/25",
                "office": "Tokyo",
                "extn": "8422"
            }]
    }
    return jsonify(data)


@home.route('/contracts', methods=['GET', 'POST'])
def contracts():
    form = ContractForm()
    form.customer_id.choices = [(g.id, (g.first_name + '' + g.last_name))
                                for g in Customer.query.order_by('first_name')]
    form.product_id.choices = [(g.id, g.name)
                               for g in Product.query.order_by('name')]
    if form.validate_on_submit():
        contract = Contract(customer_id=form.customer_id.data,
                            product_id=form.product_id.data)
        db.session.add(contract)
        db.session.commit()
        flash('contract successfully created')
        return redirect(url_for('home.index'))
    return render_template('home/contracts.html', title='Contracts', form=form)


@home.route('/transactions', methods=['GET', 'POST'])
def transactions():
    form = TransactionForm()
    form.try_contract.customer_id.choices = [(g.id, (g.first_name + '' + g.last_name))
                                             for g in Customer.query.order_by('first_name')]
    form.try_contract.product_id.choices = [(g.id, g.name)
                                            for g in Product.query.order_by('name')]
    if form.validate_on_submit():
        contract = Contract.query.filter_by(customer_id=form.try_contract.customer_id.data).filter_by(
            product_id=form.try_contract.product_id.data).first_or_404()
        print(contract)
        transaction = Transaction(
            status=form.status.data, type=form.type.data, amount=form.amount.data, contract_id=contract.id)
        db.session.add(transaction)
        db.session.commit()
        flash('transaction successfully created')
        return redirect(url_for('home.index'))
    return render_template('home/transactions.html', title='Transactions', form=form)
