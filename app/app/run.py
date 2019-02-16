# run.py
import time
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src import create_app, db
# from dbinit import database_initialization_sequence

if __name__ == '__main__':
    app = create_app()
    # with app.app_context():
    #     database_initialization_sequence()
    app.run(debug=True, host='0.0.0.0')
