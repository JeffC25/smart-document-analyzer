from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from werkzeug.utils import secure_filename
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def createApp():
    # configure flask
    from dotenv import load_dotenv
    import os

    load_dotenv('.env')
    secretKey = os.getenv('SECRET_KEY')

    app = Flask(__name__)
    app.config['SECRET_KEY'] = secretKey
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['TRAP_HTTP_EXCEPTIONS']=True
    db.init_app(app)

    # register routes
    from .views import views
    from .auth import auth
    from .api import api
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(api, url_prefix='/api/')

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