import pytest
from page_objects.AdminLoginPage import LoginAsAdmin
import time
from page_objects.AdminPage import AdminPage
from page_objects.RegistryPage import RegistryPage
from page_objects.MainPage import MainPage
from helpers import generate_random_user
from helpers import random_product


BASE_URL = 'http://192.168.44.153:8081'
ADMIN_URL = f'{BASE_URL}/admin'
ADMIN_LOGIN = 'user'
ADMIN_PASSWORD = 'bitnami'
TEST_PATTERN = '_test_'


@pytest.mark.parametrize("i", range(5))
def test_reg_user(browser, i):
    browser.get(BASE_URL)
    reg_page = RegistryPage(browser)
    reg_page.click_register()
    user_data = generate_random_user()
    reg_page.register_user(user_data)
    time.sleep(0.1)
    assert "Your Account Has Been Created!" in browser.page_source


@pytest.fixture(scope='function')
def admin_login(browser):
    browser.get(ADMIN_URL)
    login_page = LoginAsAdmin(browser)
    login_page.log_as_admin(ADMIN_LOGIN, ADMIN_PASSWORD)


@pytest.mark.parametrize("i", range(2))
def test_add_product(browser, admin_login, i):
    admin_page = AdminPage(browser)
    product_data = random_product(TEST_PATTERN)
    admin_page.add_product(product_data)
    assert TEST_PATTERN in admin_page.name_of_first_product()
    admin_page.delete_test_prod(TEST_PATTERN)


@pytest.mark.parametrize("i", range(2))
def test_del_product(browser, admin_login, i):
    admin_page = AdminPage(browser)
    product_data = random_product(TEST_PATTERN)
    admin_page.add_product(product_data)
    admin_page.delete_test_prod(TEST_PATTERN)
    time.sleep(0.5)
    assert TEST_PATTERN not in admin_page.name_of_first_product()


@pytest.mark.parametrize("currency", ["gbp", "eur", "usd"])
def test_of_currency_btn(browser, currency):
    browser.get(BASE_URL)
    main_page = MainPage(browser)
    main_page.chose_currency(currency)
    assert main_page.actual_currency_symbol() in main_page.get_first_product_price()
