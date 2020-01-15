from features.service.model.service_response_model import *
from marshmallow import ValidationError
from helpers.utils import schema_failure
from libs.micro_services.base_micro_service import *
from random import randint

'''
We make a Model of the different operation, generating custom class for each operation
In this case there are common function inherited from BaseMicroService Class
'''

class Template(BaseMicroService):

    def __init__(self, context):
        BaseMicroService.__init__(self)
        self.context = context
        self.base_url = "https://jsonplaceholder.typicode.com/"

    def send_request(self, message):
        self.operation = message
        self.send()

    def default_response(self, result):
        if result == 'OK':
            if self.response.status_code != 200:
                assert False, self.micro_service + " Wrong HTTP Status code: " + str(self.response.status_code)
        else:
            self.wrong_response(result)


class ResourceGet(Template):
    def __init__(self, context):
        Template.__init__(self, context)
        self.request.verb = "GET"
        self.request.base_url = self.base_url + "todos"

    def send_resource_get(self, message):
        self.operation = message
        self.send_request(message)

    def check_resource_get(self, result='OK'):
        self.default_response(result)
        if self.response.status_code == 200:
            validate_get_resource(self.response.body)

    def get_random_resource_id(self):
        list_id = []
        for resource in self.response.body:
            if 'id' in resource:
                list_id.append(resource['id'])
        random_id = int(randint(0, len(list_id) - 1))
        return str(list_id[random_id])


class ResourceGetId(Template):
    def __init__(self, context, id):
        Template.__init__(self, context)
        self.request.verb = "GET"
        self.request.base_url = self.base_url + "todos/"
        self.append_parameter(id)
        self.id = id

    def send_resource_get_id(self, message):
        self.operation = message
        self.send_request(message)

    def check_resource_get_id(self, result):
        self.default_response(result)
        if self.response.status_code == 200:
            validate_get_resource_id(self.response.body)

    def get_random_resource_id(self):
        list_id = []
        for resource in self.response.body:
            if 'id' in resource:
                list_id.append(resource['id'])
        random_id = int(randint(0, len(list_id) - 1))
        return str(list_id[random_id])


'''
To validate the correct structure, the code call to the marshmallow classes where we define the type and structure
of the different operation response
'''


def validate_get_resource(response,):
    try:
        TodosSchema(many=True).load(response)
    except ValidationError as err:
        schema_failure(err.messages,response)


def validate_get_resource_id(response,):
    try:
        TodosSchema().load(response)
    except ValidationError as err:
        schema_failure(err.messages,response)