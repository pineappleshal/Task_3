import allure

from pages.account_page import AccountPage
from pages.feed_page import FeedPage
from pages.history_page import HistoryPage


@allure.feature('Лента заказов')
class TestFeed:
    @allure.title('Открытие деталей заказа из ленты')
    def test_open_order_details(self, driver, existing_order):
        page = FeedPage(driver).open()
        page.wait_for_order(existing_order)
        page.open_order(existing_order)
        assert page.modal_is_visible()
        assert page.modal_order_number() == existing_order
        assert page.modal_has_ingredients()

    @allure.title('Заказ из истории пользователя отображается в общей ленте')
    def test_history_order_appears_in_feed(self, driver, authorized_constructor, existing_order):
        authorized_constructor.go_to_account()
        AccountPage(driver).go_to_history()
        history = HistoryPage(driver)
        history_numbers = history.wait_for_order(existing_order)
        history.go_to_feed()
        feed_numbers = FeedPage(driver).wait_for_order(existing_order)
        assert existing_order in history_numbers and existing_order in feed_numbers

    @allure.title('Новый заказ увеличивает счётчик за всё время')
    def test_total_counter_increases(self, driver, authorized_constructor):
        authorized_constructor.go_to_feed()
        page = FeedPage(driver)
        before = page.total()
        page.go_to_constructor()
        authorized_constructor.build_burger()
        number = authorized_constructor.place_order()
        authorized_constructor.close_modal()
        authorized_constructor.go_to_feed()
        page.wait_for_order(number)
        assert page.wait_total_above(before) > before

    @allure.title('Новый заказ увеличивает счётчик за сегодня')
    def test_today_counter_increases(self, driver, authorized_constructor):
        authorized_constructor.go_to_feed()
        page = FeedPage(driver)
        before = page.today()
        page.go_to_constructor()
        authorized_constructor.build_burger()
        number = authorized_constructor.place_order()
        authorized_constructor.close_modal()
        authorized_constructor.go_to_feed()
        page.wait_for_order(number)
        assert page.wait_today_above(before) > before

    @allure.title('Новый заказ отображается в разделе В работе')
    def test_new_order_in_progress(self, driver, authorized_constructor):
        authorized_constructor.build_burger()
        number = authorized_constructor.place_order()
        authorized_constructor.close_modal()
        authorized_constructor.go_to_feed()
        assert number in FeedPage(driver).wait_in_progress(number)
