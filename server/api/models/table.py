# from tortoise.models import Model
# from tortoise import fields

from tortoise import Model, fields

class Table(Model):
    id = fields.IntField(primary_key=True)
    name = fields.TextField()
    description = fields.TextField()


    def __str__(self):
        return f"{self.name}"
