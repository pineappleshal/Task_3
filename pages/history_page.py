from locators.account_locators import HistoryLocators
from pages.base_page import BasePage


class HistoryPage(BasePage):
    def is_open(self):
        self.wait_path('/account/order-history')
        return self.is_visible(HistoryLocators.ACTIVE_HISTORY)

    def order_numbers(self):
        return [int(value.lstrip('#')) for value in self.texts(HistoryLocators.ORDER_NUMBERS)]

    def wait_for_order(self, number):
        def matching_orders():
            numbers = self.order_numbers()
            return numbers if number in numbers else False
        return self.wait_for(matching_orders)
