import pytest
from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import sync_playwright

#Import features where the test steps are located
scenarios('features/login.feature')

#Shared fixtures, important to initiate browser, context and page considering the text logic will be into Cucumber features
#Opening browser
@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()

#Opening page
@pytest.fixture
def context_page(browser):
    page = browser.new_page()
    yield page
    page.close()


#Given
@given("I am on the login page")
def go_to_login(context_page):
    context_page.goto("https://practicetestautomation.com/practice-test-login/") 


#When
@when("I log in with valid credentials")
def perform_login(context_page):
    context_page.fill("input[id='username']", "student")
    context_page.fill("input[id='password']", "Password123")
    context_page.click("button[id='submit']")

#Then
@then("I should see the Welcome page")
def validate_dashboard(context_page):
    assert context_page.is_visible("text=Logged In Successfully")  