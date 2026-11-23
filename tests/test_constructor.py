import allure

from pages.constructor_page import ConstructorPage
from pages.feed_page import FeedPage


@allure.feature('Конструктор')
class TestConstructor:
    @allure.title('Переход по ссылке Конструктор')
    def test_open_constructor(self, driver):
        FeedPage(driver).open().go_to_constructor()
        assert ConstructorPage(driver).is_open()

    @allure.title('Переход по ссылке Лента заказов')
    def test_open_feed(self, driver):
        ConstructorPage(driver).open().go_to_feed()
        assert FeedPage(driver).is_open()

    @allure.title('Открытие деталей ингредиента')
    def test_open_ingredient_details(self, driver):
        page = ConstructorPage(driver).open()
        name = page.bun_name()
        page.open_bun_details()
        assert page.modal_is_visible()
        assert page.ingredient_details_name() == name

    @allure.title('Закрытие деталей ингредиента крестиком')
    def test_close_ingredient_details(self, driver):
        page = ConstructorPage(driver).open()
        page.open_bun_details()
        page.close_modal()
        assert not page.modal_is_visible()

    @allure.title('Добавление ингредиента увеличивает счётчик')
    def test_ingredient_counter_increases(self, driver):
        page = ConstructorPage(driver).open()
        before = page.sauce_count()
        page.add_sauce()
        assert page.sauce_count() == before + 1

    @allure.title('Авторизованный пользователь оформляет заказ')
    def test_place_order(self, authorized_constructor):
        authorized_constructor.build_burger()
        number = authorized_constructor.place_order()
        assert number > 0
        assert authorized_constructor.confirmation_text() == 'Ваш заказ начали готовить'
