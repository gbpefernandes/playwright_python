import pytest
import asyncio
from playwright.async_api import async_playwright

#Initiating async execution
@pytest.mark.asyncio
async def run_location_emulation(url, longitude, latitude, filename="screenshot_location_emulation.png"):
    #Starting asyncronous execution
    async with async_playwright() as p:
        #Starting browser (on headed mode), page and context using geolocation and permissions
        browser = await p.chromium.launch(headless=False, slow_mo=50)
        context = await browser.new_context(
            geolocation={"longitude": longitude, "latitude":latitude},
            permissions=["geolocation"]
        )

        #In order for the browser to have the location it is needed to grant permission
        await context.grant_permissions(["geolocation"])

        #Starting new page
        page = await context.new_page()

        #Visiting URL passed as parameter
        await page.goto(url)

        #Clicking on "Find my location" button
        await page.click("#find-loc")

        #Retrieving zoom in button object, to zoom in the map
        zoom_in = page.get_by_role("button", name="Zoom in")

        #Logic to press the zoom in button until it is no longer enabled (max zoom)
        #Considering .html wasn't coded to be disabled when max zoom, only the attribute of the class was disabled
        #So the logic needed to refresh the attribute at every iteration
        while True:
            button_classes = await zoom_in.get_attribute("class") or ""
            if "disabled" in button_classes:
                #Printing to return the if statement ending the loop
                print("Button disabled - already max zoom.")
                break
            await zoom_in.click()
            #Timeout of 0.5s just to be more appealing to the user checking the implementation
            await page.wait_for_timeout(500) 

        #Saving and printing current user agent to check if emulation is successfull
        user_agent = await page.evaluate("() => navigator.userAgent")
        print(f"User Agent: {user_agent}")

        #Taking a screenshot only of the map object and saving it
        map = page.locator("id=latlongmap")
        await map.screenshot(path=filename)

        #Closing browser, context and messaging user
        await context.close()
        await browser.close()
        print(f"Screenshot saved to {filename}")

if __name__ == "__main__":
    #Manually coding longitude, latitude and URL, just to avoid entering them hardcoded on the function
    longitude = -46.47377889945316
    latitude = -23.545418169964286
    url = "https://maps.ie/coordinates.html"

    #Calling function and sending coordinates, URL, and using default filename
    asyncio.run(run_location_emulation(url, longitude, latitude))