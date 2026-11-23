import allure

from locators.account_locators import AccountLocators
from pages.base_page import BasePage


class AccountPage(BasePage):
    def open(self):
        return super().open('/account')

    def profile_name(self):
        self.wait_for(lambda: self.attribute(AccountLocators.NAME, 'value') != 'Загрузка...')
        return self.attribute(AccountLocators.NAME, 'value')

    @allure.step('Перейти в историю заказов')
    def go_to_history(self):
        self.click(AccountLocators.HISTORY)

    @allure.step('Выйти из аккаунта')
    def logout(self):
        self.click(AccountLocators.LOGOUT)
