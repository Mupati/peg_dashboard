from flask import render_template, jsonify, flash, redirect, url_for, request
from . import home
from .forms import ProductForm, CustomerForm, ContractForm, TransactionForm
from .. import db
from ..models import Product, Customer, Contract, Transaction
import json
from flask_login import login_required
from sqlalchemy.orm import joinedload


@home.route('/index')
@home.route('/')
@login_required
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
        return 'Added {}'.format(form.first_name.data + ' ' + form.last_name.data)
    return render_template('home/customers.html', form=form, title='Customer')


@home.route('/customer_data')
def fetch_customers_information():
    customers = Customer.query.all()
    customer_data = [customer.to_json() for customer in customers]
    data = {
        "data": customer_data
    }
    return jsonify(data)


@home.route('/customer/update/', methods=['POST'])
def update_customer():
    form_data = []
    for data in request.form.values():
        form_data.append(data)
    customer = Customer.query.get_or_404(form_data[0])
    form = CustomerForm(obj=customer)
    customer.first_name = form_data[1]
    customer.last_name = form_data[2]
    db.session.commit()
    return 'updated'


@home.route('/customer/delete/', methods=['POST'])
def delete_customer():
    request_form = request.form
    for key in request_form.keys():
        data = key
    customer = Customer.query.get_or_404(data)
    db.session.delete(customer)
    db.session.commit()
    return 'deleted'


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
def fetch_products_information():
    products = Product.query.all()
    product_data = [product.to_json() for product in products]
    data = {
        "data": product_data
    }
    return jsonify(data)


@home.route('/product/update/', methods=['POST'])
def update_product():
    form_data = []
    for data in request.form.values():
        form_data.append(data)
    product = Product.query.get_or_404(form_data[0])
    form = ProductForm(obj=product)
    product.name=form_data[1],
    product.deposit=form_data[2],
    product.total_price=form_data[3],
    product.payment_frequency=form_data[4],
    product.payment_amount=form_data[5]
    db.session.commit()
    return 'updated'


@home.route('/product/delete/', methods=['POST'])
def delete_product():
    request_form = request.form
    for key in request_form.keys():
        data = key
    productId = json.loads(data)
    finalId = productId['id']
    product = Product.query.get_or_404(finalId)
    db.session.delete(product)
    db.session.commit()
    flash('You have successfully deleted the product.')
    return jsonify({'status', 'delete sucess'})


@home.route('/contracts', methods=['GET', 'POST'])
def contracts():
    form = ContractForm()
    form.customer_id.choices = [(g.id, (g.first_name + '  ' + g.last_name))
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


@home.route('/contract_data')
def fetch_contracts_information():
    contracts = db.session.query(Contract.id, Product.name, Customer.first_name + ' '+Customer.last_name, Contract.created_at).join(
        Product, Contract.product_id == Product.id).join(Customer, Contract.customer_id == Customer.id).all()
    contract_data = [{'id': contract[0], 'product_id': contract[1], 'customer_id': contract[2],
                      'created_at': contract[3].strftime('%Y-%m-%d %H:%M:%S')} for contract in contracts]
    data = {
        "data": contract_data
    }
    return jsonify(data)


@home.route('/contract/delete/', methods=['POST'])
def delete_contract():
    request_form = request.form
    for key in request_form.keys():
        data = key
    contractId = json.loads(data)
    finalId = contractId['id']
    contract = Contract.query.get_or_404(finalId)
    db.session.delete(contract)
    db.session.commit()
    flash('You have successfully deleted the customer.')
    return jsonify({'status', 'delete sucess'})


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
        transaction = Transaction(
            status=form.status.data, type=form.type.data, amount=form.amount.data, contract_id=contract.id)
        db.session.add(transaction)
        db.session.commit()
        flash('transaction successfully created')
        return redirect(url_for('home.index'))
    return render_template('home/transactions.html', title='Transactions', form=form)


@home.route('/transaction_data')
def fetch_transactions_information():
    transactions = Transaction.query.all()
    transaction_data = [transaction.to_json() for transaction in transactions]
    print(transaction_data)
    data = {
        "data": transaction_data
    }
    # print(data)
    return jsonify(data)


@home.route('/transaction/delete/', methods=['POST'])
def delete_transaction():
    request_form = request.form
    for key in request_form.keys():
        data = key
    transactionId = json.loads(data)
    finalId = transactionId['id']
    transaction = Transaction.query.get_or_404(finalId)
    db.session.delete(transaction)
    db.session.commit()
    flash('You have successfully deleted the customer.')
    return jsonify({'status', 'delete sucess'})
