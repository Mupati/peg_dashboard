from flask import render_template, jsonify
from . import home


@home.route('/index')
@home.route('/')
def index():
    return render_template('home/index.html')


@home.route('/customers')
def customers():
    return render_template('home/customers.html')


@home.route('/products')
def products():
    return render_template('home/products.html')


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


@home.route('/contracts')
def contracts():
    return render_template('home/contracts.html')


@home.route('/transactions')
def transactions():
    return render_template('home/transactions.html')
