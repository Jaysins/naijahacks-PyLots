# coding=utf-8
"""
view
"""
from flask_login import logout_user, login_required, login_user, current_user
from flask import render_template, send_from_directory, request, jsonify, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
# noinspection PyUnresolvedReferences
from forms import RegisterForm, LoginForm
# noinspection PyUnresolvedReferences
from app import app, db, login_manager
# noinspection PyUnresolvedReferences
from models import User, Business


@login_manager.user_loader
def load_user(user_id):
    """

    :param user_id:
    :return:
    """
    # noinspection PyUnresolvedReferences
    return User.query.get(int(user_id))


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """
    signup route
    :return:
    """
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        print('validate', request.form)
        username = form.name.data.title()
        email = form.email.data.capitalize()
        business = form.business.data.title()
        language = form.language.data.title()
        password = generate_password_hash(form.password.data, method='sha256')
        check_valid = User.query.filter_by(name=username).first()
        if check_valid is None:
            check_valid = User.query.filter_by(email=email).first()
        if check_valid is not None:
            return render_template('signup.html', error='Username, Email or address already taken', form=form)
        
        new_user = User(name=username, email=email, password=password,
                       language=language, verified=True)
        
        db.session.add(new_user)
        db.session.commit()
        
        new_bus = Business(name=business, user_id=new_user.id)
        db.session.add(new_bus)
        db.session.commit()
        return redirect(url_for('login'))
    else:
        print(form.errors)
    return render_template('signup.html', form=form, error='')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """

    :return:
    """

    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        username = form.name.data.title()
        email = form.name.data.capitalize()
        password = form.password.data
        user = User.query.filter_by(name=username).first()
        if user is None:
        	user = User.query.filter_by(email=email).first()
        if user is None:
        	return render_template('login.html', error='Username or Email does not exist', form=form)
        if user.verified is False:
        	return "you have not been verified yet"
        if check_password_hash(user.password, password):
        	login_user(user)
        if user.is_admin is True:
        	return 'admin'
        return f'welcome {username}'
    else:
    	print(form.errors)
    return render_template('login.html', form=form, error='')


@app.route('/logout')
@login_required
def logout():
    """

    :return:
    """
    logout_user()
    return redirect(url_for('index'))