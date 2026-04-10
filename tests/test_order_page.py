import allure
from pages.order_page import OrderPage


class TestOrder:

    def create_order(self, page):
        page.add_ingredients()
        page.place_order()
        number = page.get_order_number()
        if not number.startswith('0'):
            number = '0' + number
        page.close_order_modal()
        return number

    @allure.title('Номер заказа отображается в - В работе')
    def test_order_appears_in_progress(self, logged_in_browser):
        page = OrderPage(logged_in_browser)
        order_num = self.create_order(page)
        page.move_to_feed_js()
        in_feed = page.get_orders_in_progress()
        assert order_num == in_feed

    @allure.title('Счётчик "Всего" увеличивается')
    def test_total_counter_increases(self, logged_in_browser):
        page = OrderPage(logged_in_browser)
        page.move_to_feed()
        initial_text = page.get_total_count()
        initial = int(initial_text)
        page.move_to_constructor()
        self.create_order(page)
        page.move_to_feed_js()
        updated_text = page.wait_for_text_change(page.locators.ORDERS_DONE_TOTAL,initial_text,timeout=10)
        updated = int(updated_text)
        assert updated > initial, f"Счётчик 'Всего' не увеличился: было {initial}, стало {updated}"        

    @allure.title('Счётчик "Сегодня" увеличивается')
    def test_today_counter_increases(self, logged_in_browser):
        page = OrderPage(logged_in_browser)
        page.move_to_feed()
        initial_text = page.get_today_count()
        initial = int(initial_text)
        page.move_to_constructor()
        self.create_order(page)
        page.move_to_feed_js()
        updated_text = page.wait_for_text_change(page.locators.ORDERS_DONE_TODAY,initial_text,timeout=10)
        updated = int(updated_text)
        assert updated > initial, f"Счётчик 'Сегодня' не увеличился: было {initial}, стало {updated}"
