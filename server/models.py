from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from flask import Flask, request, jsonify, make_response
from sqlalchemy.orm import validates, relationship
# from config import db, bcrypt
from server.config import db, bcrypt
from sqlalchemy import Column, Integer, String

# db.init_app(app)
import re

# Models go here!

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    serialize_only = ('id', 'username')

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    _hash_password = db.Column(db.String(128), nullable=False)

    user_products = db.relationship('UserProduct', back_populates='user', cascade='all,delete-orphan')

    @property
    def password(self):
        raise ArithmeticError('password is read only')
    
    @password.setter
    def password(self, password):
        pattern = re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&*]).{8,}$')
        if not password or not isinstance(password, str):
            raise ValueError('password is required and must be a string')
        if not pattern.match(password):
            raise ValueError('password must be at least 8 characters and includes at least one upper case, one lower case letter and one symbol')
        self._hash_password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self._hash_password, password)
    
    @validates('username')
    def validate_username(self,key, username):
        if not username or not isinstance(username, str):
            raise ValueError('Username is required and must be a string.')
        if len(username) < 5 or len(username) > 50:
            raise ValueError('Username must be between 5 and 50 characters inclusive.')
        return username
    
    
        
class Product(db.Model, SerializerMixin):
    __tablename__ = 'products'
    serialize_only = ('id', 'name', 'description', 'image', 'price')

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    image = db.Column(db.String)
    price = db.Column(db.Numeric(10,2), nullable=False)

    user_products = db.relationship('UserProduct', back_populates='product', cascade='all,delete-orphan')


class UserProduct(db.Model, SerializerMixin):
    __tablename__ = 'user_products'
    serialize_only = ('id', 'user_id', 'product_id', 'quantity', 'delivery_address', 'payment_method')


    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)
    delivery_address = db.Column(db.String(255), nullable=False)
    payment_method = db.Column(db.String(50), nullable=False)
    
    user = db.relationship('User', back_populates='user_products')
    product = db.relationship('Product', back_populates='user_products')  