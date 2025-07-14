import json
import pytest
from playwright.async_api import async_playwright

#Initiating async execution
@pytest.mark.asyncio
async def test_api():
    #Starting asyncronous execution
    async with async_playwright() as p:
        #Starting browser (on headless mode)
        browser = await p.chromium.launch(headless=False)
        
        #Starting context with sending the API URL as base_url
        context = await browser.new_context(base_url="https://reqres.in")
 
        #Adding request to API on users/3 and sending the header to allow one request (free request)
        response = await context.request.get("/api/users/3", headers={"x-api-key": "reqres-free-v1"})
       
        #Using json to collect text from the response
        response_body = json.loads(await response.text())

        #Printing response status (for debugging) and then asserting if it is equal to 200
        print(f"\n{response.status}")
        assert response.status == 200

        #Printing response body (for debugging) and then asserting if its ID is equal to 3
        print(response_body)
        assert response_body["data"]["id"] == 3
        
        #Closing browser and context
        await context.close()
        await browser.close()

