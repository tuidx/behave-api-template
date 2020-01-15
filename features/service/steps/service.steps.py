from behave import *
from features.service.model.service import ResourceGet, ResourceGetId

'''
This step file its the "glue" code between Gherkins feature definition and the coding into Python
Behave search the translate from feature file searching the matching in the step directory
We use a class model and "move" the data between steps with the behave context object
'''


# GET
@given("a get resource")
def step_impl(context):
    context.get_resource = ResourceGet(context)


@when("user send the get resource request")
def step_impl(context):
    context.get_resource.send_resource_get("Sending Get Resource")


@then("user receive the get resource response")
def step_impl(context):
    context.get_resource.check_resource_get()


# GET ID
@given("a get {resource_id}")
def step_impl(context,resource_id):
    context.get_resource_id = ResourceGetId(context, resource_id)


@when("user send the get resource_id request")
def step_impl(context):
    context.get_resource_id.send_resource_get_id("Sending Get Resource ID")


@then("user receive the get resource_id response {result}")
def step_impl(context, result):

    context.get_resource_id.check_resource_get_id(result)
