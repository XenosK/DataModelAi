from tortoise.models import Model
from tortoise import fields


class Field(Model):
    id = fields.IntField(primary_key=True)
    tid = fields.IntField()
    name = fields.TextField()
    description = fields.TextField()
    type_enum = fields.IntField()
