from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'launch Chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome()

@when(u'open google home page')
def home_page(context):
    context.driver.get("https://www.google.co.in/")
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)

@then(u'verify that the logo present on page')
def logo_verification(context):
    logo_status = context.driver.find_element(By.XPATH, "//img[@alt='Google']").is_displayed()
    assert logo_status is True
    print("Test Pass")

@then(u'close the browser')
def close_browser(context):
    context.driver.close()

