import allure

from locators.auth_locators import ForgotPasswordLocators
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):
    def open(self):
        return super().open('/forgot-password')

    @allure.step('Запросить восстановление пароля для тестового пользователя')
    def restore(self, email):
        self.fill(ForgotPasswordLocators.EMAIL, email)
        self.click(ForgotPasswordLocators.RESTORE)

    def is_open(self):
        return self.wait_path('/forgot-password') == '/forgot-password' and self.is_visible(ForgotPasswordLocators.RESTORE)
