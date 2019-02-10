# app/src/translator/__init__.py

from flask import Blueprint

translator = Blueprint('translator', __name__)

from . import routes
