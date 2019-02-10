# app/src/carts/__init__.py

from flask import Blueprint

carts = Blueprint('carts', __name__)

from . import routes