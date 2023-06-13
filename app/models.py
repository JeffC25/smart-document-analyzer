from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# database will be created in __init__.py

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))
    username = db.Column(db.String(128))
    files = db.relationship('File')

class File(db.Model):
    __tablename__ = 'file'
    id = db.Column(db.Integer, primary_key=True)
    fileName = db.Column(db.String(128))
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))
    fileSize = db.Column(db.Integer)
    fileSummary = db.Column(db.String(128))
    timeStamp = db.Column(db.DateTime(timezone=True), default=func.now())

class Keyword(db.Model):
    __tablename__ = 'keyword'
    id = db.Column(db.Integer, primary_key=True)
    keyword = db.Column(db.String(128))

class KeywordPair(db.Model):
    __tablename__ = 'pair'
    id = db.Column(db.Integer, primary_key=True)
    keywordId = db.Column(db.Integer, db.ForeignKey('keyword.id'))
    fileId = db.Column(db.Integer, db.ForeignKey('file.id'))