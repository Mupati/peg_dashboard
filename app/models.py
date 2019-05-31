from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager
from datetime import datetime


class Employee(UserMixin, db.Model):

    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'))
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    is_admin = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('access denied')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Employee: {}>'.format(self.first_name + ' ' + self.last_name)

# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return Employee.query.get(int(user_id))


class Department(db.Model):
    """
    Create a Department table
    """

    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    employees = db.relationship('Employee', backref='department',
                                lazy='dynamic')

    def __repr__(self):
        return '<Department: {}>'.format(self.name)


class Role(db.Model):
    """
    Create a Role table
    """

    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    employees = db.relationship('Employee', backref='role',
                                lazy='dynamic')

    def __repr__(self):
        return '<Role: {}>'.format(self.name)


class Country(db.Model):
    """
    Create a Country Table
    """

    __tablename__ = 'countries'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    employees = db.relationship('Employee', backref='country', lazy='dynamic')

    def __repr__(self):
        return '<Country: {}'.format(self.name)


class Customer(db.Model):

    __tablename__ = 'customers'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    first_name = db.Column(db.String(60), index=True, nullable=False)
    last_name = db.Column(db.String(60), index=True, nullable=False)
    contracts = db.relationship('Contract', backref='customer', lazy='dynamic')

    def to_json(self):
        return dict(id=self.id,
                    first_name=self.first_name,
                    last_name=self.last_name)

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
    contracts = db.relationship('Contract', backref='product', lazy='dynamic')

    def to_json(self):
        return dict(id=self.id,
                    name=self.name,
                    deposit=self.deposit,
                    total_price=self.total_price,
                    payment_frequency=self.payment_frequency,
                    payment_amount=self.payment_amount
                    )

    def __repr__(self):
        return'<Product {}>'.format(self.name)


class Contract(db.Model):

    __tablename__ = 'contracts'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, index=True,
                           default=datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    transactions = db.relationship('Transaction', backref='contract', lazy='dynamic')

    def to_json(self):
        return dict(id=self.id,
                    product_id=self.product_id,
                    customer_id=self.customer_id,
                    created_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S')
                    )

    def __repr__(self):
        return'<Contract number {}>'.format(self.id)


class Transaction(db.Model):

    __tablename__ = 'transactions'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    status = db.Column(db.String(60), index=True, nullable=False)
    type = db.Column(db.String(60), nullable=False)
    amount = db.Column(db.Float)
    date = db.Column(
        db.DateTime, default=datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'))
    contract_id = db.Column(db.Integer, db.ForeignKey('contracts.id'))

    def to_json(self):
        return dict(id=self.id,
                    status=self.status,
                    type=self.type,
                    amount=self.amount,
                    date=self.date.strftime('%Y-%m-%d %H:%M:%S'),
                    contract_id=self.contract_id
                    )

    def __repr__(self):
        return'<Transaction number {}>'.format(self.id)
