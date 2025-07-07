from sanic import Sanic
from sanic import Sanic, text



from sanic_cors import CORS
from tortoise.contrib.sanic import register_tortoise

from api import api
# from sanic_openapi import swagger_blueprint
from api.config.log_settings import LOG_SETTINGS
# app = Sanic(__name__, LOG_SETTINGS)
app = Sanic("test")
app.blueprint(api, name_prefix="app")
# CORS(app)
# CORS(app, origins="*", allow_headers="*", supports_credentials=True)
# app.blueprint(swagger_blueprint)

from textwrap import dedent

app.ext.openapi.describe(
    "Testing API",
    version="1.2.3",
    description=dedent(
        """
        # Info
        This is a description. It is a good place to add some _extra_ doccumentation.

        **MARKDOWN** is supported.
        """
    ),
)
app.config.API_VERSION = '1.0.0'
app.config.API_TITLE = 'DataModelAiApi'
app.config.API_DESCRIPTION = '数据模型ai API'
app.config.API_PRODUCES_CONTENT_TYPES = ['application/json']
from api.models import Table
register_tortoise(
    app,
    config_file="db.json",
    generate_schemas=True
)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
