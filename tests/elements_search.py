from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


class MainPageLocators:
    SEARCH_RESULT_LINK = (By.CSS_SELECTOR, 'div#content h4 a')
    SEARCH_INPUT = (By.CSS_SELECTOR, 'div#search input[name="search"]')
    CART_BUTTON = (By.CSS_SELECTOR, 'div#cart button')
    TABLETS_BUTTON = (By.CSS_SELECTOR, '#menu a[href="http://192.168.44.153:8081/tablet"]')
    ABOUT_US_BUTTON = (By.CSS_SELECTOR, 'footer a[href="http://192.168.44.153:8081/about_us"]')


@pytest.mark.parametrize("locator", [
    MainPageLocators.SEARCH_RESULT_LINK,
    MainPageLocators.SEARCH_INPUT,
    MainPageLocators.CART_BUTTON,
    MainPageLocators.TABLETS_BUTTON,
    MainPageLocators.ABOUT_US_BUTTON,
])
def test_for_main_page(browser, locator):
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable(locator))


class SelectorsForCatalogPage:
    GRID_VIEW_BUTTON = (By.CSS_SELECTOR, '#grid-view')
    LIST_VIEW_BUTTON = (By.CSS_SELECTOR, '#list-view')
    PALM_TREO_PRO_LINK = (By.CSS_SELECTOR, '#input-sort')
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, 'button[onclick^="cart.add"]')
    LOGO = (By.CSS_SELECTOR, 'div#logo')


def test_for_catalog_page(browser):
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable(SelectorsForCatalogPage.GRID_VIEW_BUTTON))
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable(SelectorsForCatalogPage.LIST_VIEW_BUTTON))
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable(SelectorsForCatalogPage.PALM_TREO_PRO_LINK))
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable(SelectorsForCatalogPage.ADD_TO_CART_BUTTON))
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable(SelectorsForCatalogPage.LOGO))


class SelectorsForProductCardPage:
    DESCRIPTION = (By.CSS_SELECTOR, 'a[href="#tab-description"]')
    SPECIFICATION = (By.CSS_SELECTOR, 'a[href="#tab-specification"]')
    REVIEW = (By.CSS_SELECTOR, 'a[href="#tab-review"]')
    ADD_TO_WISH_LIST = (By.CSS_SELECTOR, 'button[onclick*="wishlist.add"]')
    COMPARE_PRODUCT = (By.CSS_SELECTOR, 'button[onclick*="compare.add"]')


def test_of_product_card_page(browser):
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable(SelectorsForProductCardPage.DESCRIPTION))
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable(SelectorsForProductCardPage.SPECIFICATION))
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable(SelectorsForProductCardPage.REVIEW))
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable(SelectorsForProductCardPage.ADD_TO_WISH_LIST))
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable(SelectorsForProductCardPage.COMPARE_PRODUCT))


class SelectorsForAdminLoginPage:
    LOGIN_BUTTON = (By.CSS_SELECTOR, '.btn.btn-primary')
    INPUT_USERNAME = (By.XPATH, '//input[@id="input-username"]')
    INPUT_PASSWORD = (By.XPATH, '//input[@id="input-password"]')
    FORGOTTEN_PASSWORD_BUTTON = (By.CSS_SELECTOR, '.help-block a')
    HEADER_LOGO = (By.CSS_SELECTOR, '#header-logo')


def test_of_admin_login_page(browser):
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable(SelectorsForAdminLoginPage.LOGIN_BUTTON))
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable(SelectorsForAdminLoginPage.INPUT_USERNAME))
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable(SelectorsForAdminLoginPage.INPUT_PASSWORD))
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable(SelectorsForAdminLoginPage.FORGOTTEN_PASSWORD_BUTTON))
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable(SelectorsForAdminLoginPage.HEADER_LOGO))


class SelectorsForRegistrationPage:
    CONTINUE_BUTTON = (By.CSS_SELECTOR, 'input[value="Continue"]')
    FIRST_NAME = (By.CSS_SELECTOR, '#input-firstname')
    LAST_NAME = (By.CSS_SELECTOR, '#input-lastname')
    PASSWORD = (By.CSS_SELECTOR, '#input-password')
    AGREE_PP = (By.XPATH, '//input[@name="agree"]')


def test_for_registration_page(browser):
    selectors = [SelectorsForRegistrationPage.CONTINUE_BUTTON,
                 SelectorsForRegistrationPage.FIRST_NAME,
                 SelectorsForRegistrationPage.LAST_NAME,
                 SelectorsForRegistrationPage.PASSWORD,
                 SelectorsForRegistrationPage.AGREE_PP]

    for selector in selectors:
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable(selector))
