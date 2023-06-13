from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from .database import *
from . import db

# validate signup/login
def isValidPassword(password1, password2):
    if password1 != password2:
        flash('Passwords do not match.', category='error')
        return False
    if len(password1) < 8 or len(password1) > 32:
        flash('Password must be between 8 and 32 characters', category='error')
        return False
    return True

def isValidUsername(username):
    if not username.isalnum():
        flash('Username must only contain letters and numbers.', category='error')
        return False
    if len(username) < 4 or len(username) > 32:
        flash('Username must be between 4 and 32 characters.', category='error')
        return False
    user = getUserByUsername(username)
    if user:
        flash('Username already exists.', category='error')
    return True

def isValidEmail(email):
    user = getUserByEmail(email)
    if user:
        flash('Email already in use', category='error')
        return False
    return True

def authenticate(user, password, email):
    return check_password_hash(user.password, password + email)

# define routes
auth = Blueprint('auth', __name__)

# error handler
@auth.errorhandler(404)
def page_not_found(e):
    return render_template('not_found.html'), 404

# login
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

# logout
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Successfully logged out!', category='success')
    return redirect(url_for('auth.login'))

# sign up
@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if isValidEmail(email) and isValidUsername(username) and isValidPassword(password1, password2):
            newUser = createUser(email, username, password1)
            login_user(newUser)
            
            flash('Account created!', category='success')
            return redirect(url_for('views.article'))

    return render_template("signup.html", user=current_user)