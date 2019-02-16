# third-party imports
import time
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

DBUSER = 'jose'
DBPASS = 'joseShopify'
DBHOST = 'db'
DBPORT = '5432'
DBNAME = 'testdb'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{db}'.format(
        user=DBUSER,
        passwd=DBPASS,
        host=DBHOST,
        port=DBPORT,
        db=DBNAME)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.url_map.strict_slashes = False
app.secret_key = DBPASS
db = SQLAlchemy(app)

def create_app():

    # db.init_app(app)

    from .routes.translator import translator as translator_blueprint
    app.register_blueprint(translator_blueprint)

    # dbstatus = False
    # while dbstatus == False:
    #     try:
    #         db.create_all()
    #     except:
    #         time.sleep(2)
    #     else:
    #         dbstatus = True
    return app
