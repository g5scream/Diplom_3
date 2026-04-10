import allure
from locators.order_locators import OrderLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout=20)
        self.locators = OrderLocators()

    @allure.step('Добавить ингредиенты в конструктор')
    def add_ingredients(self):
        self.drag_and_drop_ingredient(self.locators.INGREDIENT_BUN, self.locators.BURGER_CONSTRUCTOR)
        self.drag_and_drop_ingredient(self.locators.INGREDIENT_SOUCE, self.locators.BURGER_CONSTRUCTOR)

    @allure.step('Оформить заказ')
    def place_order(self):
        self.wait_for_element_clickable(self.locators.ORDER_BUTTON)
        self.click_on_element(self.locators.ORDER_BUTTON)

    @allure.step('Закрыть модальное окно заказа')
    def close_order_modal(self):
        self.wait_for_element_clickable(self.locators.CLOSE_MODAL_BUTTON)
        self.click_via_js(self.locators.CLOSE_MODAL_BUTTON)
        self.wait_for_element_not_visible(self.locators.ORDER_OVERLAIN_MODAL)

    @allure.step('Перейти в "Ленту заказов" (JS)')
    def move_to_feed_js(self):
        super().move_to_order_feed(use_js=True)

    @allure.step('Перейти в "Конструктор"')
    def move_to_constructor(self):
        super().move_to_constructor()

    @allure.step('Перейти в "Ленту заказов"')
    def move_to_feed(self):
        super().move_to_order_feed(use_js=False)

    @allure.step('Получить номер заказа из "В работе"')
    def get_orders_in_progress(self):
        return self.get_element_text(self.locators.ORDERS_IN_PROGRESS_NUMBERS)

    @allure.step('Получить счётчик "Всего"')
    def get_total_count(self):
        return self.get_element_text(self.locators.ORDERS_DONE_TOTAL)

    @allure.step('Получить счётчик "Сегодня"')
    def get_today_count(self):
        return self.get_element_text(self.locators.ORDERS_DONE_TODAY)

    @allure.step('Получить номер заказа')
    def get_order_number(self):
        initial = self.get_element_text(self.locators.ID_ORDER)
        self.wait_for_counter_change(
            counter_func=lambda: self.get_element_text(self.locators.ID_ORDER),
            initial_value=initial,
            timeout=15
        )
        return self.get_element_text(self.locators.ID_ORDER)
