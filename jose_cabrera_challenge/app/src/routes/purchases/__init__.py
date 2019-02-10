# app/src/purchases/__init__.py

from flask import Blueprint

purchases = Blueprint('purchases', __name__)

from . import routes