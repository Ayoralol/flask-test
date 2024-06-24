from config import Config
from flask_sqlalchemy import SQLAlchemy # type: ignore
from flask import Flask # type: ignore

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        from . import routes, models
        db.create_all()

    return app