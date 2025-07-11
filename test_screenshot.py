import re
from playwright.sync_api import Page, sync_playwright

def take_screenshot(url, filename="screenshot.png"):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        page.screenshot(path=filename)
        browser.close()
        print(f"Screenshot saved to {filename}")

if __name__ == "__main__":
    take_screenshot("https://uol.com.br")