import allure
import pytest

from helpers.browser_factory import BrowserFactory
from helpers.stellar_api import StellarApi
from pages.constructor_page import ConstructorPage
from pages.login_page import LoginPage


def pytest_addoption(parser):
    parser.addoption('--browser', choices=['chrome', 'firefox', 'all'], default='all')
    parser.addoption('--headed', action='store_true', help='Показывать окно тестового браузера')


def pytest_generate_tests(metafunc):
    if 'browser_name' in metafunc.fixturenames:
        selected = metafunc.config.getoption('--browser')
        names = ['chrome', 'firefox'] if selected == 'all' else [selected]
        metafunc.parametrize('browser_name', names)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.failed and 'driver' in item.funcargs:
        allure.attach(item.funcargs['driver'].get_screenshot_as_png(),
                      f'Ошибка: {report.when}', allure.attachment_type.PNG)


@pytest.fixture
def driver(request, browser_name):
    browser = BrowserFactory.create(browser_name, headless=not request.config.getoption('--headed'))
    allure.dynamic.label('browser', browser_name)
    yield browser
    browser.quit()


@pytest.fixture
def user_api():
    api = StellarApi()
    user = api.create_user()
    yield api, user
    try:
        api.delete_user()
    finally:
        api.close()


@pytest.fixture
def user(user_api):
    return user_api[1]


@pytest.fixture
def authorized_constructor(driver, user):
    LoginPage(driver).open().login(user['email'], user['password'])
    page = ConstructorPage(driver)
    page.is_open()
    return page


@pytest.fixture
def existing_order(user_api):
    return user_api[0].create_order()
