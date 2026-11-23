import allure

from locators.auth_locators import LoginLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def open(self):
        return super().open('/login')

    def login(self, email, password):
        with allure.step('Войти под тестовым пользователем'):
            self.fill(LoginLocators.EMAIL, email)
            self.fill(LoginLocators.PASSWORD, password)
            self.click(LoginLocators.LOGIN)
            self.wait_path('/')

    @allure.step('Перейти к восстановлению пароля')
    def go_to_password_recovery(self):
        self.click(LoginLocators.RESTORE)

    def is_open(self):
        return self.wait_path('/login') == '/login' and self.is_visible(LoginLocators.LOGIN)
