from flask import Flask
from sqlalchemy import create_engine

from api.v1 import v1

# from connection import conn
# from model.subscription import hello

def create_app():
    app = Flask(__name__)
    
    print("Result fetched successfully")
    
    app.register_blueprint(v1)
    
    @app.route("/")
    def index():
        return "hello how are you!"
    
    return app


create_app()
