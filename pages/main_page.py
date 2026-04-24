import allure
from helpers.urls import Urls
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Перейти в "Конструктор"')
    def move_to_constructor(self):
        self.open_page(Urls.FEED_URL)
        super().move_to_constructor()

    @allure.step('Перейти в "Ленту заказов"')
    def move_to_feed(self):
        self.open_page(Urls.BASE_URL)
        super().move_to_order_feed(use_js=False)

    @allure.step('Открыть модальное окно ингредиента')
    def open_ingredient_modal(self):
        self.open_page(Urls.BASE_URL)
        self.click_on_element(self.locators.FLUOR_BUN)
        self.wait_for_element_visible(self.locators.MODAL)

    @allure.step('Проверить, что модальное окно открыто')
    def modal_open(self):
        return self.element_displayed(self.locators.MODAL)

    @allure.step('Закрыть модальное окно по крестику')
    def close_ingredient_modal(self):
        self.click_on_element(self.locators.MODAL_CLOSE)
        self.wait_for_element_not_visible(self.locators.MODAL)

    @allure.step('Проверить, что модальное окно закрыто')
    def modal_closed(self):
        return self.element_hidden(self.locators.MODAL)

    @allure.step('Добавить булку в конструктор')
    def add_bun(self):
        self.drag_and_drop_ingredient(self.locators.INGREDIENT_BUN, self.locators.BURGER_CONSTRUCTOR)

    @allure.step('Добавить соус в конструктор')
    def add_sauce(self):
        self.drag_and_drop_ingredient(self.locators.INGREDIENT_SOUCE, self.locators.BURGER_CONSTRUCTOR)

    @allure.step('Получить счётчик соуса')
    def get_sauce_counter(self):
        return self.get_element_text(self.locators.INGREDIENT_COUNTER)
    