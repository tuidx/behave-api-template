from marshmallow import Schema, fields
'''
Use of the marshmallow library to map the structure of the response object of the "Todos" resource
https://marshmallow.readthedocs.io/en/stable/
'''


class TodosSchema(Schema):
   userId = fields.Integer(required=True)
   id = fields.Integer(required=True)
   title = fields.String(required=True)
   completed = fields.Boolean(required=True)
