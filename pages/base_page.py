import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from locators.base_locators import BaseLocators
from locators.order_locators import OrderLocators


class BasePage:
    def __init__(self, driver, timeout=30):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)  
        self.locators = BaseLocators()

    @allure.step('Открыть по URL')
    def open_page(self, url):
        self.driver.get(url)

    @allure.step('Ожидание видимости элемента')
    def wait_for_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    @allure.step('Ожидание исчезновения элемента')
    def wait_for_element_not_visible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    @allure.step('Ожидание кликабельности элемента')
    def wait_for_element_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))
    
    @allure.step('Клик по элементу')
    def click_on_element(self, locator):
        self.wait_for_element_clickable(locator).click()

    @allure.step('Проверить, что элемент отображается')
    def element_displayed(self, locator):
        return self.wait_for_element_visible(locator).is_displayed()

    @allure.step('Перетащить ингредиент в конструктор')
    def drag_and_drop_ingredient(self, source_locator, target_locator):
        source = self.wait_for_element_visible(source_locator)
        target = self.wait_for_element_visible(target_locator)
        actions = ActionChains(self.driver)
        actions.click_and_hold(source).move_to_element(target).release().perform()
        self.driver.execute_script("arguments[1].dispatchEvent(new Event('drop', { bubbles: true }));", source, target)

    @allure.step('Получить текст элемента')
    def get_element_text(self, locator):
        return self.wait_for_element_visible(locator).text

    @allure.step('Получить текущий URL')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Проверить, что элемент скрыт/отсутствует')
    def element_hidden(self, locator):
        elements = self.driver.find_elements(*locator)
        return len(elements) == 0 or not elements[0].is_displayed()

    @allure.step('Заполнить поле текстом')
    def fill_field(self, locator, text):
        element = self.wait_for_element_visible(locator)
        element.clear()
        element.send_keys(text)

    @allure.step('Выполнить авторизацию')
    def login(self, email, password):
        wait = WebDriverWait(self.driver, 5)
        try:
            wait.until(lambda driver: len(driver.find_elements(*OrderLocators.ORDER_OVERLAIN_MODAL)) == 0) # две модалки, запускаются через раз
        except:
            pass
        self.click_on_element(BaseLocators.LOGIN_BUTTON)
        self.fill_field(BaseLocators.EMAIL_FIELD, email)
        self.fill_field(BaseLocators.PASS_FIELD, password)
        login_button = wait.until(
            EC.element_to_be_clickable(BaseLocators.LOGIN_BUTTON)
        )
        login_button.click()
        
    @allure.step('Клик через JavaScript')
    def click_via_js(self, locator):
        element = self.wait_for_element_visible(locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Дождаться изменения счётчика')
    def wait_for_counter_change(self, counter_func, initial_value, timeout=15):
        return self.wait.until(
            lambda _: counter_func() != initial_value,
            message=f"Счётчик не изменился от {initial_value} за {timeout} сек"
        )

    @allure.step('Дождаться изменения текста элемента')       # Firefox - счётчик всего/сегодня"                    
    def wait_for_text_change(self, locator, initial_text, timeout=15):
        def text_has_changed(driver):
            current_text = self.get_element_text(locator)
            return current_text if current_text != initial_text else False
        return self.wait.until(
            text_has_changed,
            message=f"Текст не изменился от '{initial_text}' за {timeout} сек"
        )

    @allure.step('Перейти в "Конструктор"')
    def move_to_constructor(self):
        modal_wait = WebDriverWait(self.driver, 5)
        try:
            modal_wait.until(
            lambda driver: len(driver.find_elements(*OrderLocators.ORDER_OVERLAIN_MODAL)) == 0)   # две модалки
        except:
            pass  
        self.click_on_element(self.locators.CONSTRUCTOR_BUTTON)
        self.wait_for_element_visible(self.locators.INGREDIENT_BUN)  

    @allure.step('Перейти в "Ленту заказов"')
    def move_to_order_feed(self, use_js=False):
        click_func = self.click_via_js if use_js else self.click_on_element
        click_func(self.locators.ORDER_FEED_BUTTON)
        self.wait_for_element_visible(self.locators.TITLE_FEED)
