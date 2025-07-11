import re
import pytest
import asyncio
from playwright.async_api import async_playwright, expect, Page

#Initiating async execution
@pytest.mark.asyncio
async def test_perform_register_and_login():
    #Starting asyncronous execution
    async with async_playwright() as p:
        #Starting browser (on headed mode), page and context
        browser = await p.chromium.launch(headless=False, slow_mo=50)
        context = await browser.new_context()
        page = await browser.new_page()

        #Visiting URL passed on function parameter
        await page.goto("https://bugbank.netlify.app/")

        #Clicking 'Register' button
        await page.click('text="Registrar"', button='left', force=True, timeout=45000)

        #Filling register information
        await page.type('div.card__register input[name="email"]', "gabriel-fernandes@gmail.com")
        await page.type('div.card__register input[name="name"]', "Gabriel")
        await page.type('div.card__register input[name="password"]', "teste123")
        await page.type('div.card__register input[name="passwordConfirmation"]', "teste123")
        #await page.click('div.card__register id="toggleAddBalance"', button='left', force=True, timeout=45000)

        #Clicking 'Confirm' button
        await page.click('text="Cadastrar"', button='left', force=True, timeout=45000)

        #Returning to initial URL to perform sign-in
        await page.goto("https://bugbank.netlify.app/")

        #Filling sign-in information
        await page.type('input[name="email"]', "gabriel-fernandes@gmail.com")
        await page.type('input[name="password"]', "teste123")

        #Clicking 'Confirm' button
        await page.click('text="Acessar"', button='left', force=True, timeout=10000000)

        #First assess to verify if login occurred without issues
        title_locator = page.locator('meta[property="og:title"]')
        await expect(title_locator).to_have_attribute("content", "BugBank")

        #Second assess to verify if login occurred without issues
        welcome_locator = page.get_by_text("bem vindo ao BugBank :)")
        await expect(welcome_locator).to_be_visible()

        #Storing state (cache and origin) for future access
        await context.storage_state(path="state.json")

        #Closing browser
        await browser.close()

