from tortoise.models import Model
from tortoise import fields


class CatalogAi(Model):
    id = fields.IntField(primary_key=True)
    name = fields.TextField(description='Ai目录名称')
    description = fields.TextField(description='Ai目录介绍')
    notes = fields.TextField(description='业务过程相关描述')
    tables = fields.JSONField(description='涉及的表模型')

