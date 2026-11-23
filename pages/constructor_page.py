import allure

from config import ORDER_TIMEOUT
from locators.constructor_locators import ConstructorLocators as L
from pages.base_page import BasePage


class ConstructorPage(BasePage):
    def is_open(self):
        self.visible(L.TITLE)
        return self.wait_path('/') == '/'

    @allure.step('Открыть детали первой булки')
    def open_bun_details(self):
        self.click(L.FIRST_BUN)
        self.visible(L.INGREDIENT_TITLE)
        self.visible(L.INGREDIENT_NAME)

    def bun_name(self):
        return self.text(L.BUN_NAME)

    def ingredient_details_name(self):
        return self.text(L.INGREDIENT_NAME)

    def sauce_count(self):
        return int(self.text(L.SAUCE_COUNTER))

    @allure.step('Добавить соус в конструктор')
    def add_sauce(self):
        count = self.sauce_count()
        self.drag(L.FIRST_SAUCE, L.BASKET)
        self.wait_for(lambda: self.sauce_count() == count + 1)

    @allure.step('Собрать бургер')
    def build_burger(self):
        self.drag(L.FIRST_BUN, L.BASKET)
        self.wait_for(lambda: int(self.text(L.BUN_COUNTER)) == 2)
        self.add_sauce()

    @allure.step('Оформить заказ')
    def place_order(self):
        self.click(L.PLACE_ORDER)
        self.wait_for(lambda: self.is_visible(L.ORDER_CONFIRMATION), timeout=ORDER_TIMEOUT)
        self.wait_for(lambda: self.text(L.ORDER_NUMBER).isdigit()
                      and int(self.text(L.ORDER_NUMBER)) not in (0, 9999), timeout=ORDER_TIMEOUT)
        return int(self.text(L.ORDER_NUMBER))

    def confirmation_text(self):
        return self.text(L.ORDER_CONFIRMATION)
