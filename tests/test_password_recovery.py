import allure

from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage
from pages.reset_password_page import ResetPasswordPage


@allure.feature('Восстановление пароля')
class TestPasswordRecovery:
    @allure.title('Переход по ссылке восстановления пароля')
    def test_open_password_recovery(self, driver):
        LoginPage(driver).open().go_to_password_recovery()
        assert ForgotPasswordPage(driver).is_open()

    @allure.title('Ввод почты и переход к сбросу пароля')
    def test_send_recovery_email(self, driver, user):
        ForgotPasswordPage(driver).open().restore(user['email'])
        assert ResetPasswordPage(driver).is_open()

    @allure.title('Значок показа пароля активирует поле')
    def test_password_visibility_activates_field(self, driver, user):
        ForgotPasswordPage(driver).open().restore(user['email'])
        page = ResetPasswordPage(driver)
        page.wait_path('/reset-password')
        page.toggle_password()
        assert page.password_is_active()
        assert page.password_type() == 'text'
