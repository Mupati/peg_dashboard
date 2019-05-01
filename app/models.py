from app import db
from datetime import datetime


class Customer(db.Model):

    __tablename__ = 'customers'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    first_name = db.Column(db.String(60), index=True, nullable=False)
    last_name = db.Column(db.String(60), index=True, nullable=False)
    # contract = db.relationship('Contract', backref='customer', lazy=True)

    def __repr__(self):
        return '<Customer {}>'.format(self.first_name + ' ' + self.last_name)


class Product(db.Model):

    __tablename__ = 'products'

    id = db.Column(db.Integer, autoincrement=True,  primary_key=True)
    name = db.Column(db.String(60), unique=True, index=True, nullable=False)
    deposit = db.Column(db.Float)
    total_price = db.Column(db.Float)
    payment_frequency = db.Column(db.String(60), index=True, nullable=False)
    payment_amount = db.Column(db.Float)
    # contract = db.relationship('Product', backref='product', lazy=True)

    def __repr__(self):
        return'<Product {}>'.format(self.name)


class Contract(db.Model):

    __tablename__ = 'contracts'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, index=True,
                           default=datetime.utcnow)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    # transaction = db.relationship(
    #     'Transaction', backref='contract', lazy=True)

    def __repr__(self):
        return'<Contract number {}>'.format(self.id)


class Transaction(db.Model):

    __tablename__ = 'transactions'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    status = db.Column(db.String(60), index=True, nullable=False)
    type = db.Column(db.String(60), nullable=False)
    amount = db.Column(db.Float)
    date = db.Column(db.DateTime)
    contract_id = db.Column(db.Integer, db.ForeignKey('contracts.id'))

    def __repr__(self):
        return'<Transaction number {}>'.format(self.id)
