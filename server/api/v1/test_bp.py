from sanic.response import json
from sanic import Blueprint

test_bp = Blueprint('test', url_prefix='/test')


# http://127.0.0.1:5000/v1/api/test
@test_bp.route('/')
async def test(request):
    return json({'hello': 'world'})

@test_bp.route('/server/employees', methods=['GET'], name="root")
async def test2(request):
    response = json({"items":[{"id":1,"name":"Edward Perry","age":25,"joinDate":"2025-07-03T05:10:10.693Z","role":"Finance"},

                              {"id":3,"name":"Cody Phillips","age":19,"joinDate":"2025-07-03T05:10:10.693Z","role":"Development"}],
                     "itemCount":3
                     }
                    )
    # response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@test_bp.route('/server/employees/<id>', methods=['GET'], name="root2")
async def test3(request, id):
    print(id)
    response = json({"id":1,
                     "name":"Edward Perry",
                     "age":25,
                     "joinDate":"2025-07-03T08:48:10.637Z",
                     "role":"Finance"
                     }
                    )
    # response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@test_bp.route('/server/employees', methods=['POST'], name="root3")
# @doc.summary('更新指标')
# @doc.consumes(, location="body")
async def metrics_app(request):
    print(request.json)
    # try:
    #     update_metrics(request.json)
    #     return json({"status": 1, "info":"更新成功"})
    # except Exception as e:
    return json({"status": 1, "info":"更新成功"})
