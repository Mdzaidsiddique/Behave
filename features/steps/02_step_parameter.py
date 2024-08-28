from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'I Launch Chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome()

@when(u'I Open orange HRM homepage')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)


@when(u'Enter username "{user}" and password "{pswd}"')
def step_impl(context, user, pswd):
    context.driver.find_element(By.NAME, "username").send_keys(user)
    context.driver.find_element(By.NAME, "password").send_keys(pswd)

@when(u'Click on login button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[@type='submit']").click()


@then(u'User must successfully login to dashboard page')
def step_impl(context):
    try:
        dashboard_text = context.driver.find_element(By.XPATH, " //h6[normalize-space()='Dashboard']").text
    except:
        context.driver.close()
        assert False, "Test Fail"

    if dashboard_text == "Dashboard":
        context.driver.close()
        assert True, "Test Pass"

