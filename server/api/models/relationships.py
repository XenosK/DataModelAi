from tortoise.models import Model
from tortoise import fields


class Relationships(Model):
    id = fields.IntField(primary_key=True)
    table_start = fields.TextField()
    field__start = fields.TextField()
    table_end = fields.TextField()
    field_end = fields.TextField()

