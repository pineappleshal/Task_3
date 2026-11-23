import allure

from pages.account_page import AccountPage
from pages.history_page import HistoryPage
from pages.login_page import LoginPage


@allure.feature('Личный кабинет')
class TestAccount:
    @allure.title('Переход в личный кабинет из конструктора')
    def test_open_account(self, driver, authorized_constructor, user):
        authorized_constructor.go_to_account()
        assert AccountPage(driver).profile_name() == user['name']

    @allure.title('Переход в историю заказов')
    def test_open_order_history(self, driver, authorized_constructor):
        authorized_constructor.go_to_account()
        AccountPage(driver).go_to_history()
        assert HistoryPage(driver).is_open()

    @allure.title('Выход из аккаунта')
    def test_logout(self, driver, authorized_constructor):
        authorized_constructor.go_to_account()
        AccountPage(driver).logout()
        assert LoginPage(driver).is_open()
