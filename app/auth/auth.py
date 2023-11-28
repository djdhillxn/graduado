from flask import Blueprint, render_template, request, url_for, flash, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.models import User
from app import db
from flask_login import login_user, logout_user, login_required
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
from wtforms.validators import Email, Regexp

class RegistrationForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [Email(), validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [validators.DataRequired()])


class LoginForm(FlaskForm):
    username = StringField('Username', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])

auth = Blueprint('auth', __name__)


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, password_hash=hashed_password)
        
        existing_user = User.query.filter((User.username == form.username.data) | (User.email == form.email.data)).first()
        if existing_user:
            flash('Username or email already exists.')
            return redirect(url_for('auth.signup'))

        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful!')
        return redirect(url_for('auth.login'))
    return render_template('register.html', form=form)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            return redirect(url_for('main.dashboard'))
        else:
            flash('Invalid username or password')
    return render_template('login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
