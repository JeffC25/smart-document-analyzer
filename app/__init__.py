from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database.db"

def createApp():
    from dotenv import load_dotenv
    import os

    load_dotenv('.env')
    secretKey = os.getenv('SECRET_KEY')

    app = Flask(__name__)
    app.config['SECRET_KEY'] = secretKey
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app

