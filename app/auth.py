from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db
from .database import *

# verify user login
def authenticate(user, password, email):
    return check_password_hash(user.password, password + email)

# define routes
auth = Blueprint('auth', __name__)

@auth.errorhandler(404)
def page_not_found(e):
    return render_template('not_found.html'), 404

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = getUserByEmail(email)
        if user and authenticate(user, password, email):
            flash('Login successful!', category='success')

            login_user(user)
            return redirect(url_for('views.article'))
        else:
            flash('Invalid login. Please try again.', category='error')

    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = getUserByEmail(email)

        if user:
            flash('Email already exists.', category='error')
        elif len(username) < 3:
            flash('Username must be greater than 3 characters.', category='error')
        elif password1 != password2:
            flash('Passwords do not match.', category='error')
        elif len(password1) < 5:
            flash('Password must be at least 5 characters.', category='error')
        else:
            newUser = createUser(email, username, password1)

            login_user(newUser)
            flash('Account created!', category='success')
            return redirect(url_for('views.article'))

    return render_template("signup.html", user=current_user)