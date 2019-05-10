from flask import render_template, jsonify, flash, redirect, url_for, request
from . import home
from .forms import ProductForm, CustomerForm, ContractForm, TransactionForm
from .. import db
from ..models import Product, Customer, Contract, Transaction
import json


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
    if request.method == 'POST':
        customer = Customer(first_name=form.first_name.data,
                            last_name=form.last_name.data)
        db.session.add(customer)
        db.session.commit()
        flash('customer successfully added')
        return redirect(url_for('home.index'))
    return render_template('home/customers.html', form=form, title='Customer')


@home.route('/customer_data')
def fetch_customers_information():
    customers = Customer.query.all()
    customer_data = [customer.to_json() for customer in customers]
    data = {
        "data": customer_data
    }
    return jsonify(data)


@home.route('/customers/update/<int:id>', methods=['GET', 'POST'])
def update_customer(id):
    customer = Customer.query.get_or_404(id)
    form = CustomerForm(obj=customer)
    if form.validate_on_submit():
        customer.first_name = form.first_name.data
        customer.last_name = form.last_name.data
        db.session.commit()
        flash('You have successfully updated the customer.')
        return redirect(url_for('home.customers'))

    form.first_name.data = customer.first_name
    form.last_name.data = customer.last_name
    return render_template('home/customers.html', form=form, title='Customer')


@home.route('/customer/delete/', methods=['POST'])
def delete_customer():
    request_form = request.form
    for key in request_form.keys():
        data = key
    customerId = json.loads(data)
    finalId = customerId['id']
    customer = Customer.query.get_or_404(finalId)
    db.session.delete(customer)
    db.session.commit()
    flash('You have successfully deleted the customer.')
    return jsonify({'status', 'delete sucess'})


@home.route('/products', methods=['GET', 'POST'])
def products():
    """
    Render the product table and 
    Add products to the products table from here
    """
    form = ProductForm()
    if request.method == 'POST':
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
    form.customer_id.choices = [(g.id, (g.first_name + '' + g.last_name))
                                for g in Customer.query.order_by('first_name')]
    form.product_id.choices = [(g.id, g.name)
                               for g in Product.query.order_by('name')]
    if request.method == 'POST':
        contract = Contract(customer_id=form.customer_id.data,
                            product_id=form.product_id.data)
        db.session.add(contract)
        db.session.commit()
        flash('contract successfully created')
        return redirect(url_for('home.index'))
    return render_template('home/contracts.html', title='Contracts', form=form)


@home.route('/contract_data')
def fetch_contracts_information():
    contracts = Contract.query.all()
    print(contracts)
    contract_data = [contract.to_json() for contract in contracts]
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
    if request.method == 'POST':
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
    data = {
        "data": transaction_data
    }
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
