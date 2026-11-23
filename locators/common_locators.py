from selenium.webdriver.common.by import By


class CommonLocators:
    ACCOUNT = (By.LINK_TEXT, 'Личный Кабинет')
    CONSTRUCTOR = (By.LINK_TEXT, 'Конструктор')
    FEED = (By.LINK_TEXT, 'Лента Заказов')
    MODAL = (By.CSS_SELECTOR, '[class*="Modal_modal_opened"]')
    MODAL_CLOSE = (By.CSS_SELECTOR, '[class*="Modal_modal_opened"] button[class*="Modal_modal__close"]')
