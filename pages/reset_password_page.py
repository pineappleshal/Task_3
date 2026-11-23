import allure

from locators.auth_locators import ResetPasswordLocators
from pages.base_page import BasePage


class ResetPasswordPage(BasePage):
    @allure.step('Нажать значок показа пароля')
    def toggle_password(self):
        self.click(ResetPasswordLocators.PASSWORD_ICON)

    def is_open(self):
        return self.wait_path('/reset-password') == '/reset-password' and self.is_visible(ResetPasswordLocators.SAVE)

    def password_is_active(self):
        return 'input_status_active' in self.attribute(ResetPasswordLocators.PASSWORD_CONTAINER, 'class')

    def password_type(self):
        return self.attribute(ResetPasswordLocators.PASSWORD, 'type')
