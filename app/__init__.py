from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .models import db

migrate = Migrate()


def create_app():
    # make the Flask app
    app = Flask(__name__)

    # set up the database path
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # connect the database
    db.init_app(app)

    # connect migrate to the app and db
    migrate.init_app(app, db)

    # bring in routes from routes.py
    from .routes import api
    app.register_blueprint(api)

    # return the app so i can run it
    return app
