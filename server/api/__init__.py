# api/__init__.py

from sanic import Blueprint
from .v1 import v1

api = Blueprint.group(v1, name_prefix="api", url_prefix='/api')
