import os
import json
from datetime import datetime
import allure

'''
Auxiliary function to help in the test execution
'''


# Function to log the request and response to a defined log
def trace_request(log_name,titulo, operation, arg1="", arg2="", arg3="", arg4="", arg5="", arg6=""):
    directory = "logs"
    ft = open(directory + os.sep + log_name + ".log", "a")
    mensaje = ""
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if arg1 != "":
        mensaje += "|" + str(arg1).replace("\n", "").replace("\r", "")
    if arg2 != "":
        mensaje += "|" + str(arg2).replace("\n", "").replace("\r", "")
    if arg3 != "":
        mensaje += "|" + str(arg3).replace("\n", "").replace("\r", "")
    if arg4 != "":
        mensaje += "|" + str(arg4).replace("\n", "").replace("\r", "")
    if arg5 != "":
        mensaje += "|" + str(arg5).replace("\n", "").replace("\r", "")
    if arg6 != "":
        mensaje += "|" + str(arg6).replace("\n", "").replace("\r", "")
    ft.write(fecha + "|" + operation + "|" + titulo + mensaje + "\n")
    ft.close()


# @@@@@@@@@@ TREAT JSON
def dict_to_str(json_object):
    try:
        response = json.dumps(json_object)
    except (ValueError, TypeError):
        response = str(json_object)
    return response


def exist_att(object, field):
    try:
        getattr(object,field)
        return True
    except AttributeError:
        return False


# Trace Errors
def schema_failure(message, response):
    allure.attach(dict_to_str(response), name="response_error")
    assert False, str(message)
