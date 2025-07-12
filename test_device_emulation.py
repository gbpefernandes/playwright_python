import pytest
import asyncio
from playwright.async_api import async_playwright

#Initiating async execution
@pytest.mark.asyncio
async def run_device_emulation(url, filename="screenshot_device_emulation.png"):
    #Starting asyncronous execution
    async with async_playwright() as p:
        #Creating a device object with iPhone X user agent
        #Documentation:
        #https://github.com/microsoft/playwright/blob/main/packages/playwright-core/src/server/deviceDescriptorsSource.json
        iphone_10 = p.devices['iPhone X']

        #Starting browser (on headed mode), page and context using my device emulation config
        browser = await p.chromium.launch(headless=False, slow_mo=50)
        context = await browser.new_context(
            **iphone_10,
        )
        page = await context.new_page()

        #Visiting URL passed as parameter
        await page.goto(url)

        #Saving and printing current user agent to check if emulation is successfull
        user_agent = await page.evaluate("() => navigator.userAgent")
        print("User Agent:", user_agent)

        #Saving and printing current viewport parameters to check if emulation is successfull
        viewport_size = page.viewport_size
        print("Viewport:", viewport_size)

        #Taking a screenshot and saving it
        await page.screenshot(path=filename)

        #Closing browser, context and messaging user
        await context.close()
        await browser.close()
        print(f"Screenshot saved to {filename}")

if __name__ == "__main__":
    #Calling function and sending URL, and using default filename
    asyncio.run(run_device_emulation("https://uol.com.br"))