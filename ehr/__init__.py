from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from ehr.config import Config


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()


def create_app(config_class=Config):
	application = Flask(__name__)
	application.config.from_object(Config)

	db.init_app(application)
	bcrypt.init_app(application)
	login_manager.init_app(application)
	mail.init_app(application)

	from ehr.errors.handlers import errors

	application.register_blueprint(errors)

	return application
