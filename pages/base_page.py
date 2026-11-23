from urllib.parse import urlparse

import allure
from selenium.common.exceptions import ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import BASE_URL, WAIT_TIMEOUT
from locators.common_locators import CommonLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, WAIT_TIMEOUT)

    @allure.step('Открыть страницу {path}')
    def open(self, path='/'):
        self.driver.get(BASE_URL + path)
        return self

    def visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        def click_when_ready(driver):
            element = EC.element_to_be_clickable(locator)(driver)
            if element:
                element.click()
                return True
            return False

        WebDriverWait(self.driver, WAIT_TIMEOUT, ignored_exceptions=(
            ElementClickInterceptedException, StaleElementReferenceException,
        )).until(click_when_ready)

    def fill(self, locator, value):
        element = self.visible(locator)
        element.clear()
        element.send_keys(value)

    def text(self, locator):
        return self.visible(locator).text

    def texts(self, locator):
        return WebDriverWait(self.driver, WAIT_TIMEOUT,
                             ignored_exceptions=(StaleElementReferenceException,)).until(
            lambda driver: [element.text for element in driver.find_elements(*locator)])

    def attribute(self, locator, name):
        return self.visible(locator).get_attribute(name)

    def is_visible(self, locator):
        return any(element.is_displayed() for element in self.driver.find_elements(*locator))

    def wait_hidden(self, locator):
        self.wait.until(EC.invisibility_of_element_located(locator))

    def wait_path(self, path):
        self.wait.until(lambda driver: urlparse(driver.current_url).path == path)
        return urlparse(self.driver.current_url).path

    def wait_for(self, condition, timeout=WAIT_TIMEOUT):
        return WebDriverWait(self.driver, timeout,
                             ignored_exceptions=(StaleElementReferenceException,)).until(lambda _: condition())

    def drag(self, source, target):
        start, end = self.visible(source), self.visible(target)
        self.driver.execute_script('arguments[0].scrollIntoView({block: "center"});', start)
        # React DnD использует HTML5 DataTransfer. Передаём его явно в обоих браузерах.
        self.driver.execute_script('''
            const source = arguments[0], target = arguments[1];
            const dataTransfer = new DataTransfer();
            const dispatch = (element, type) => element.dispatchEvent(
                new DragEvent(type, {bubbles: true, cancelable: true, dataTransfer}));
            dispatch(source, 'dragstart');
            dispatch(target, 'dragenter');
            dispatch(target, 'dragover');
            dispatch(target, 'drop');
            dispatch(source, 'dragend');
        ''', start, end)

    @allure.step('Перейти в личный кабинет')
    def go_to_account(self):
        self.click(CommonLocators.ACCOUNT)

    @allure.step('Перейти в конструктор')
    def go_to_constructor(self):
        self.click(CommonLocators.CONSTRUCTOR)

    @allure.step('Перейти в ленту заказов')
    def go_to_feed(self):
        self.click(CommonLocators.FEED)

    @allure.step('Закрыть всплывающее окно')
    def close_modal(self):
        self.click(CommonLocators.MODAL_CLOSE)
        self.wait_hidden(CommonLocators.MODAL)

    def modal_is_visible(self):
        return self.is_visible(CommonLocators.MODAL)
