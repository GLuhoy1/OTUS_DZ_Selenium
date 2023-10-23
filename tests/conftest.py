import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from passwords import login, password


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--headless", default="headless", action="store_true")
    parser.addoption("--base_url", default="http://192.168.44.153:8081/")
    parser.addoption("--admin_login", default=f"{login}")
    parser.addoption("--admin_password", default=f"{password}")


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
        options.add_argument('--no-sandbox')
        driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument('--headless')
        options.add_argument('--private')
        driver = webdriver.Firefox(options=options)

    driver.maximize_window()
    driver.get(request.config.getoption("--base_url"))
    yield driver

    driver.quit()


@pytest.fixture(scope='function')
def admin_password(request):
    return request.config.getoption("--admin_password")


@pytest.fixture(scope='function')
def admin_login(request):
    return request.config.getoption("--admin_login")
