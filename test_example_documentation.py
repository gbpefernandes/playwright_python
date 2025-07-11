#Example test located on Official documentation https://playwright.dev/python/docs/intro
import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    #Visit page
    page.goto("https://playwright.dev/")
    #Assert on title containing "Playwright"
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    #Visit page
    page.goto("https://playwright.dev/")
    #Click the get started link.
    page.get_by_role("link", name="Get started").click()
    #Assert to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()

