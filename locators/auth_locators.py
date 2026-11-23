from selenium.webdriver.common.by import By


class LoginLocators:
    EMAIL = (By.XPATH, '//label[text()="Email"]/following-sibling::input')
    PASSWORD = (By.CSS_SELECTOR, 'input[type="password"]')
    LOGIN = (By.XPATH, '//button[text()="Войти"]')
    RESTORE = (By.LINK_TEXT, 'Восстановить пароль')


class ForgotPasswordLocators:
    EMAIL = (By.XPATH, '//label[text()="Email"]/following-sibling::input')
    RESTORE = (By.XPATH, '//button[text()="Восстановить"]')


class ResetPasswordLocators:
    SAVE = (By.XPATH, '//button[text()="Сохранить"]')
    PASSWORD = (By.NAME, 'Введите новый пароль')
    PASSWORD_ICON = (By.XPATH, '//input[@name="Введите новый пароль"]/following-sibling::div')
    PASSWORD_CONTAINER = (By.XPATH, '//input[@name="Введите новый пароль"]/parent::div')
