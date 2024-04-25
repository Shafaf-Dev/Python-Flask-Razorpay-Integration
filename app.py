from flask import Flask
from sqlalchemy import create_engine

from connection import conn
from model.subscription import hello

def create_app():
    app = Flask(__name__)
    
    # open a cursor to perform database operations
    cur = conn.cursor()
    # print("Cursor opened successfully", cur)
    # engine = create_engine('postgresql:///tutorial.db', echo=True)
    hello()
    # Execute a database query
    cur.execute("SELECT * FROM student;")
    
    # Fetch the result
    result = cur.fetchall()
    print("Result fetched successfully")
    
    @app.route("/")
    def index():
        return result
    
    return app


create_app()
