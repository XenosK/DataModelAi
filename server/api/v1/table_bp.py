# api/v1/monitor_process_bp/flume_bp.py
from sanic import Blueprint
from sanic import text,json
from sanic.log import *
from ..models import Table
from sanic import Sanic, response

table_bp = Blueprint('table', url_prefix='/table')

@table_bp.route("/user")
async def list_all(request):
    users = await Table.all()
    return response.json({"users": [str(user) for user in users]})


@table_bp.route("/create")
async def create_table(request):

    users = await Table.all()
    return response.json({"users": [str(user) for user in users]})

