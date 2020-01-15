import allure
import json
import requests
from helpers.utils import dict_to_str, trace_request

'''
We create this base class with the general attibutes of any request/response
Save the logs, save the attachment if we are executing allure report
Manage the request and response, timeout, headers.
'''


class Request(object):
    def __init__(self):
        self.base_url = ""
        self.verb = ""
        self.body = {}
        self.headers = {}
        self.parameter = ""


class Response(object):
    def __init__(self):
        self.status_code = ""
        self.body = {}
        self.response_time = {}
        self.headers = {}
        self.item_number = ""


class BaseMicroService(object):

    def __init__(self):
        self.micro_service = str
        self.request = Request()
        self.response = Response()
        self.operation = str

    def send(self, timeout=40):
        log_name = self.context.feature.filename.split("/")[-1].replace("-", "_")
        if len(self.request.parameter) != 0:
            self.request.base_url = self.request.base_url + self.request.parameter + "/"
        allure.attach(
            "- URL:" + str(self.request.base_url) + "\n- Headers:" + dict_to_str(
                self.request.headers) + "\n- Body:" + dict_to_str(
                self.request.body), name="request")
        trace_request(log_name, "Send Request", self.operation, str(self.request.base_url),
                      dict_to_str(self.request.headers), dict_to_str(self.request.body))
        try:
            if self.request.verb.upper() == "POST":
                response = requests.post(self.request.base_url, json=(self.request.body), headers=self.request.headers,
                                         timeout=timeout)
            elif self.request.verb.upper() == "PUT":
                response = requests.put(self.request.base_url, json=(self.request.body), headers=self.request.headers,
                                        timeout=timeout)
            elif self.request.verb.upper() == "GET":
                response = requests.get(self.request.base_url, headers=self.request.headers, timeout=timeout)
            elif self.request.verb.upper() == "DELETE":
                response = requests.delete(self.request.base_url, headers=self.request.headers, timeout=timeout)
            else:
                assert False, "QA FRW Wrong Verb Configuration"
        except requests.exceptions.ChunkedEncodingError:
            assert False, "connection broken"
        except requests.exceptions.ReadTimeout:
            assert False, self.micro_service + " timeOut in request, more than 40sec in the response"
        self.response.status_code = response.status_code
        self.response.headers = response.headers
        try:
            self.response.body = json.loads(response.text)
        except ValueError:
            self.response.body = {}
        self.response.response_time = response.elapsed.total_seconds()
        self.response.item_number = len(self.response.body)

        if self.response.status_code > 204:
            allure.attach("- HTTP_Status:" + str(self.response.status_code) + "\n- Headers:" + dict_to_str(
                self.response.headers) + "\n- Body:" + dict_to_str(self.response.body), name="response")
            trace_request(log_name, "Get Response", self.operation, str(self.response.status_code),
                          dict_to_str(self.response.response_time), str(self.response.headers),
                          dict_to_str(self.response.body))
        else:
            allure.attach(
                "- HTTP_Status:" + str(self.response.status_code) + "\n- Headers:" + str(self.response.headers),
                name="response")
            trace_request(log_name, "Get Response", self.operation, str(self.response.status_code),
                          str(self.response.response_time), dict_to_str(self.response.headers))

    # HEADERS
    def append_headers(self, field, value):
        if value == 'None':
            return
        self.request.headers[field] = value

    # PARAMETERS
    def append_parameter(self, value):
        if value == 'None':
            return
        self.request.parameter = str(value)

    def wrong_response(self, result):
        if result == 'EMPTY':
            if self.response.status_code != 200:
                assert False, self.micro_service + " Wrong HTTP Status code: " + str(self.response.status_code)
            if self.response.item_number != 0:
                assert False, "Waiting Empty response"
        else:
            if result == 'NOT_ALLOW':
                http = 401
            elif result == 'NOT_FOUND':
                http = 404
            elif result == 'WRONG_REQ':
                http = 400
            if self.response.status_code != http:
                assert False, "Waiting http " + http + " and returned: " + str(self.response.status_code)
