from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_blog import config

db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    print(__name__)
    app = Flask(__name__)
    db.init_app(app)

    from flask_blog import main
    app.register_blueprint(main)
    app.config.from_object(config)

    return app
