# Playwright scripts using Python

This project showcases several **Playwright scripts using Python** programming language exploring Playwright documentation

## 🧠 Purpose

The idea of creating this repository came from reproducing test scripts I had already created based on a Udemy Playwright course I took a couple years back, but on JavaScript. So now I'm following the same course but coding the scripts apart on Python and implementing changes to understand a little bit about more about Playwright and its documentation.

---

## ⚙️ Technologies Used

- **Python 3.11+**
- `pytest` library
- `asyncio` library (for asyncronous execution)
- `pytest-playwright` (for Playwright)
- `pytest-bdd` (for Playwright integration with BDD - Gherkin)
- `.venv` virtual environment
- Some other libraries were used but all came as sublibraries from the ones above (requirements.txt)

---

## 📂 Project Structure

This repository contains:

- `test_example_documentation.py`: Documentation example
- `test_login.py`: Test script covering happy path on login (register + login)
- `test_screenshot.py`: Exploring screenshot method and its usage
- `test_device_emulation.py`: Test simulating a mobile phone emulation method available on Playwright library
- `test_location_emulation.py`: Same as before but covering location emulation and its peculiarities
- `features\login.feature`: Gherkin test instructions to run a simple login test (check test_bdd.py)
- `test_bdd.py`: Simple login test using Gherkin instructions inside Features folder
- `test_api.py`: API request test and validation 

---

## 🏃‍♂️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/gbpefernandes/playwright_python
cd your-repository
```

2. Run all test scripts using pytest:

```bash
pytest
```

Or run any script individually:
```bash
pytest test_login.py
```

You can also call some execution methods based on Pytest library:
```bash
pytest test_login.py --browser chromium --headed
```
---

## 📓 Script details

1. `test_example_documentation.py`: Simple example from documentation to make sure all the packages were downloaded and installed correctly

2. `test_login.py`: Asyncronous execution of registering + logging in on [BugBank](https://bugbank.netlify.app/). It is important to have register + login on the same test case considering BugBank is coded to not keep any registering information on cookies or cache, so every new Playwright session you would have to register again, unless you store key state on a .json file, just like it is implemented on the code

3. `test_screenshot.py`: Visiting a website and then hitting a screenshot of the main screen, and some variations on that (screenshot result is available on repository folder)

4. `test_device_emulation.py`: Exploring documentation and validating a script as if user is on a mobile phone, also recognizing user agent and viewport size, important to run other validation on the future

5. `test_location_emulation.py`: Trying out location emulation, which can be very tricky considering you need to send out geolocalization and give the proper permissions to the browser to share the permission. But once done you can simulate users from anywhere on the world, very important on Localization validation

6. `test_bdd.py`: Implementation of a test case written in Gherkin notation, located on features folder, which is translated to Playwright instructions and executed with help of pytest-bdd documentation

7. `test_api.py`: Validation of API request using Playwright, this case sends a get command to a public API and then check it is return and assert if everything went as expected

## 📄 References

[Udemy course](https://www.udemy.com/course/dominando-o-playwright/)

[Playwright documentation](https://playwright.dev/python/)

[Pytest-bdd documentation](https://pypi.org/project/pytest-bdd/)

[Pytest test runners](https://playwright.dev/python/docs/test-runners)
