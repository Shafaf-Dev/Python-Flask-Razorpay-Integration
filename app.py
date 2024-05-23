from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from api.v1 import v1
from connection import SQLALCHEMY_DATABASE_URI
from extension import db , migrate

def create_app():
    app = Flask(__name__)
    
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    
    extensions(app)
    
    # register the api points.
    app.register_blueprint(v1)
    
    return app


def extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    

create_app()
