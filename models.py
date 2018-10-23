# coding=utf-8
"""
Models
"""
# noinspection PyUnresolvedReferences

from app import db
import datetime
from flask_login import UserMixin


class User(UserMixin, db.Model):
    """
    class User
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(115), unique=True)
    email = db.Column(db.String(115), unique=True)
    password = db.Column(db.String(115), unique=True)
    language = db.Column(db.String(120))
    is_admin = db.Column(db.Boolean, default=False) 
    verified = db.Column(db.Boolean, default=False)         
    business = db.relationship('Business', backref='user', lazy='dynamic')
    

class Business(db.Model):
    """
    class Business
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), default=None)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

