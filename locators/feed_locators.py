from selenium.webdriver.common.by import By


class FeedLocators:
    TITLE = (By.XPATH, '//h1[text()="Лента заказов"]')
    ORDER_LINK = (By.XPATH, '//a[starts-with(@href,"/feed/")][.//p[text()="#0{number}"]]')
    ORDER_NUMBERS = (By.CSS_SELECTOR, 'a[href^="/feed/"] div[class*="textBox"] p.text_type_digits-default')
    MODAL_NUMBER = (By.CSS_SELECTOR, '[class*="Modal_modal_opened"] p.text_type_digits-default')
    MODAL_INGREDIENTS = (By.CSS_SELECTOR, '[class*="Modal_modal_opened"] li[class*="Modal_listItem"]')
    TOTAL = (By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p')
    TODAY = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p')
    IN_PROGRESS = (By.CSS_SELECTOR, 'ul[class*="OrderFeed_orderListReady"] li')
