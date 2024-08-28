from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

# other steps behave will recognize with step description in steps/.py files
# for example: chrome launching method will be taken care be some other .py file due to same steps description

@when(u'I Open orange HRM application')
def step_impl(context):
    pass


@when(u'Enter valid username and password')
def step_impl(context):
    pass


@when(u'click to login')
def step_impl(context):
    pass


@then(u'user must login to the Dashboard')
def step_impl(context):
    pass


@when(u'navigate to search page')
def step_impl(context):
    pass


@then(u'search page should display')
def step_impl(context):
    pass


@when(u'navigate to advance search page')
def step_impl(context):
    pass


@then(u'advance search page should display')
def step_impl(context):
    pass
