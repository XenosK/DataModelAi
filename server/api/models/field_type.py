from tortoise.models import Model
from tortoise import fields


class FieldType(Model):
    id = fields.IntField(primary_key=True)
    name = fields.TextField()
    value = fields.IntField()
    description = fields.TextField()

