# api/v1/__init__.py

from .test_bp import test_bp
from .table_bp import table_bp
from sanic import Blueprint
v1 = Blueprint.group(test_bp, table_bp, name_prefix="11", url_prefix='',  version='v1')
