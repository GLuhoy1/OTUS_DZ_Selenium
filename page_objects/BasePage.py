from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

BASE_TIME_WAIT = 5


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        element = WebDriverWait(self.driver, BASE_TIME_WAIT).until(EC.element_to_be_clickable(locator))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'auto', block: 'center', inline: 'center'});", element)
        element.click()

    def fill_strings(self, locator, data):
        element = WebDriverWait(self.driver, BASE_TIME_WAIT).until(EC.element_to_be_clickable(locator))
        self.click(locator)
        ActionChains(self.driver).pause(0.2).click(element).send_keys(data).perform()

    def wait_for_element(self, locator, timeout=BASE_TIME_WAIT):
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            return element
        except TimeoutException:
            raise TimeoutError(f"Element {locator} not found within {timeout} seconds.")

    def get_text(self, locator):
        element = WebDriverWait(self.driver, BASE_TIME_WAIT).until(EC.visibility_of_element_located(locator))
        return element.text

    def find_element(self, locator):
        element = WebDriverWait(self.driver, BASE_TIME_WAIT).until(EC.presence_of_element_located(locator))
        return element

    def find_elements(self, locator):
        elements = WebDriverWait(self.driver, BASE_TIME_WAIT).until(EC.presence_of_all_elements_located(locator))
        return elements
