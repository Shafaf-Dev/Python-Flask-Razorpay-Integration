from flask import Blueprint

# v1 blueprint
v1 = Blueprint("v1", __name__, url_prefix="/api/v1")

from .views import *
from .plan import *
