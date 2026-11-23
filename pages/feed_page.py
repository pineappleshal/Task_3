import allure

from locators.feed_locators import FeedLocators as L
from pages.base_page import BasePage


class FeedPage(BasePage):
    def open(self):
        super().open('/feed')
        self.visible(L.TITLE)
        return self

    def is_open(self):
        self.visible(L.TITLE)
        return self.wait_path('/feed') == '/feed'

    def order_numbers(self):
        return [int(text.lstrip('#')) for text in self.texts(L.ORDER_NUMBERS)]

    @allure.step('Открыть заказ {number} в ленте')
    def open_order(self, number):
        self.click((L.ORDER_LINK[0], L.ORDER_LINK[1].format(number=number)))
        self.visible(L.MODAL_NUMBER)

    def modal_order_number(self):
        return int(self.text(L.MODAL_NUMBER).lstrip('#'))

    def modal_has_ingredients(self):
        return self.is_visible(L.MODAL_INGREDIENTS)

    def wait_for_order(self, number):
        def matching_orders():
            numbers = self.order_numbers()
            return numbers if number in numbers else False
        return self.wait_for(matching_orders)

    def total(self):
        return int(self.text(L.TOTAL))

    def today(self):
        return int(self.text(L.TODAY))

    def wait_total_above(self, value):
        def increased_total():
            current = self.total()
            return current if current > value else False
        return self.wait_for(increased_total)

    def wait_today_above(self, value):
        def increased_today():
            current = self.today()
            return current if current > value else False
        return self.wait_for(increased_today)

    def in_progress_numbers(self):
        return [int(text) for text in self.texts(L.IN_PROGRESS) if text.isdigit()]

    def wait_in_progress(self, number):
        def matching_orders():
            numbers = self.in_progress_numbers()
            return numbers if number in numbers else False
        return self.wait_for(matching_orders)
