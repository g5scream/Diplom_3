from selenium.webdriver.common.by import By
from locators.base_locators import BaseLocators


class OrderLocators(BaseLocators):
# Выполнено за всё время
    ORDERS_DONE_TOTAL = (By.XPATH, "//p[contains(text(), 'Выполнено за все время')]/following-sibling::p[contains(@class, 'text_type_digits-large')]")
# Выполнено за сегодня
    ORDERS_DONE_TODAY = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня:')]/following-sibling::p[contains(@class, 'text_type_digits-large')]")
# Номер заказа
    ID_ORDER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title__2L34m') and contains(@class, 'text_type_digits-large')]")
# Кнопка закрытия
    CLOSE_MODAL_BUTTON = (By.XPATH, '//button[contains(@class, "Modal_modal__close__TnseK")]')
# Оверлей модалки
    ORDER_OVERLAIN_MODAL = (By.CSS_SELECTOR, "div.Modal_modal_overlay__x2ZCr")
# Номера заказов - В работе
    ORDERS_IN_PROGRESS_NUMBERS = (By.XPATH, "(//li[@class='text text_type_digits-default mb-2'])")
# Кнопка - Оформить заказ
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
