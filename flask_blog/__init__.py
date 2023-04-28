from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_blog.config import Config

db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    print(__name__)
    app = Flask(__name__)
    from flask_blog.main.routes import main
    app.register_blueprint(main)
    db.init_app(app)
    app.config.from_object(Config)

    return app
