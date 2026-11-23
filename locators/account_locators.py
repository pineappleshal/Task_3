from selenium.webdriver.common.by import By


class AccountLocators:
    HISTORY = (By.LINK_TEXT, 'История заказов')
    LOGOUT = (By.XPATH, '//button[text()="Выход"]')
    NAME = (By.NAME, 'Name')


class HistoryLocators:
    ACTIVE_HISTORY = (By.CSS_SELECTOR, 'a[href="/account/order-history"][class*="Account_link_active"]')
    ORDER_NUMBERS = (By.CSS_SELECTOR, 'a[href^="/account/order-history/"] div[class*="textBox"] p.text_type_digits-default')
