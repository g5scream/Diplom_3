import allure
from pages.main_page import MainPage
from helpers.urls import Urls


class TestMain:

    @allure.title('Переход в "Конструктор"')
    def test_move_to_constructor(self, browser):
        page = MainPage(browser)
        page.move_to_constructor()
        actual_url = browser.current_url
        expected_base = Urls.BASE_URL
        assert actual_url.startswith(expected_base), \
            f"Текущий URL {actual_url} не начинается с {expected_base}"    

    @allure.title('Переход в "Ленту заказов"')
    def test_move_to_feed(self, browser):
        page = MainPage(browser)
        page.move_to_feed()
        assert page.get_current_url() == Urls.FEED_URL

    @allure.title('Открытие модального окна ингредиента')
    def test_open_ingredient_modal(self, browser):
        page = MainPage(browser)
        page.open_ingredient_modal()
        assert page.modal_open()

    @allure.title('Закрытие модального окна по крестику')
    def test_close_ingredient_modal(self, browser):
        page = MainPage(browser)
        page.open_ingredient_modal()
        page.close_ingredient_modal()
        assert page.modal_closed()

    @allure.title('Счётчик ингредиента увеличивается')
    def test_ingredient_counter(self, browser):
        page = MainPage(browser)
        page.open_page(Urls.BASE_URL)
        initial = int(page.get_sauce_counter() or 0)
        page.add_bun()
        page.add_sauce()
        final = int(page.get_sauce_counter() or 0)
        assert final > initial
        