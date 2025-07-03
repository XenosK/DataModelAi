from sanic import Sanic
from sanic.response import json
from sanic_cors import CORS
app = Sanic("my-hello-world-app")
CORS(app)
@app.route('/')
async def test(request):
    return json({'hello': 'world'})

@app.route('/api/employees', methods=['GET'])
async def test2(request):
    response = json({"items":[{"id":1,"name":"Edward Perry","age":25,"joinDate":"2025-07-03T05:10:10.693Z","role":"Finance"},

                              {"id":3,"name":"Cody Phillips","age":19,"joinDate":"2025-07-03T05:10:10.693Z","role":"Development"}],
                     "itemCount":3
                     }
                )
    # response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route('/api/employees/<id>', methods=['GET'])
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

@app.route('/api/employees', methods=['POST'])
# @doc.summary('更新指标')
# @doc.consumes(, location="body")
async def metrics_app(request):
    print(request.json)
    # try:
    #     update_metrics(request.json)
    #     return json({"status": 1, "info":"更新成功"})
    # except Exception as e:
    return json({"status": 1, "info":"更新成功"})


if __name__ == '__main__':
    app.run(debug=True)
