from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.secret_key = 'secret'

    from config.config import Config
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app
