# coding=utf-8

"""
Forms package
"""

from wtforms import StringField, PasswordField, validators
from wtforms.validators import InputRequired, Length, Email, DataRequired, EqualTo
from flask_wtf import FlaskForm


class RegisterForm(FlaskForm):
    """
    Register
    """
    name = StringField('Name', validators=[InputRequired(), Length(min=4)])
    email = StringField('Email', validators=[InputRequired(), Email(message='invalid email')])    
    business = StringField('Business Name', validators=[InputRequired(), Length(min=4)])
    language = StringField('Language', validators=[InputRequired(), Length(min=4)])
    password = PasswordField('Password', validators=[InputRequired(), DataRequired(),
                                                     EqualTo('confirm', message='Passwords Dont Match'),
                                                     Length(min=8, max=80)])
    confirm = PasswordField('Repeat Password')


class LoginForm(FlaskForm):
    """
    LoginForm
    """
    name = StringField('Username', validators=[
                           InputRequired(), Length(min=4)])
    password = PasswordField('Password', validators=[
        InputRequired(), Length(min=8)])
