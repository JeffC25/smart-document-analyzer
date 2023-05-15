from flask_login import UserMixin, login_user
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db

def getUserByEmail(email):
    user = User.query.filter_by(email=email).first()
    return user

def getUserByUsername(username):
    user = User.query.filter_by(username=username).first()
    return user

def createUser(email, username, password):
    newUser = User(email=email, username=username, password=generate_password_hash(password + email, method='sha256'))
    db.session.add(newUser)
    db.session.commit()
    return newUser
