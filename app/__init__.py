from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

def createApp():
    # initiate flask
    from dotenv import load_dotenv
    import os

    load_dotenv('.env')
    secretKey = os.getenv('SECRET_KEY')

    app = Flask(__name__)
    app.config['SECRET_KEY'] = secretKey
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

        # register routes
    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # load database
    from .models import User, File
    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

# def createDatabase(app):
#     if not path.exists('app/' + DB_NAME):
#         db.create_all()
#         print('database created')
