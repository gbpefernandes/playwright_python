import re
from playwright.sync_api import Page, sync_playwright

def take_screenshot(url, filename="screenshot.png"):
    #Starting syncronous execution
    with sync_playwright() as p:
        #Starting browser (on headed mode) and page
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        #Visiting URL passed on function parameter
        page.goto(url)

        #Taking a screenshot and saving it
        page.screenshot(path=filename)

        #Closing browser and messaging user
        browser.close()
        print(f"Screenshot saved to {filename}")

if __name__ == "__main__":
    #Calling function and sending URL, and using default filename
    take_screenshot("https://uol.com.br")