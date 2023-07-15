import pytest
import os.path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions

PATH_TO_DRIVER = "/home/alex/otus_learn/Selenium/OTUS_DZ_Selenium/drivers"


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--drivers_folder", default=PATH_TO_DRIVER)
    parser.addoption("--headless", action="store_true")
    parser.addoption("--base_url", default="http://192.168.44.152:8081/")


'''на данный момент я не смог разобраться каким образом заставить селениум версии 4.10.0 работать с конкретным 
геккодрайвером, однако стоит отметить что данная фикстура работает коректно

Старался подбирать обьекты не привязанные к конкретной ссылке, поэтому часть тестов проходит даже на неправильной
странице (обьекты обладают одинаковыми локаторами на разных страницах), для избежания этого сценария
могу расширить локаторы.

при проверки коректности выполнения домашнего задания использовал фикстуры которые подкидывали каждому тесту нужный
URL, но удалил её для соответствия ТЗ'''


@pytest.fixture()
def browser(request):
    """для применения тестов на страницах отличных от главной необходимоо ввести её полный адрес в терминале"""
    browser_name = request.config.getoption("--browser")
    drivers_folder = request.config.getoption("--drivers_folder")
    headless = request.config.getoption("--headless")
    base_url = (str(request.config.getoption("--base_url")))
    driver = None
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument('--headless')
        chrome_service = ChromeService(executable_path=os.path.join(drivers_folder, "chromium.chromedriver"))
        driver = webdriver.Chrome(service=chrome_service, options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument('--headless')
        driver = webdriver.Firefox(options=options)

    driver.maximize_window()
    driver.get(base_url)
    yield driver

    driver.quit()
