import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions




def pytest_addoption(parser):
    parser.addoption("--browser", default="firefox")
    parser.addoption("--headless", action="store_true")
    parser.addoption("--base_url", default="http://192.168.44.153:8081/")


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    driver = None
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument('--headless')
        options.add_argument('--incognito')
        driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument('--headless')
        options.add_argument('-private')
        driver = webdriver.Firefox(options=options)

    driver.maximize_window()
    yield driver

    driver.quit()
