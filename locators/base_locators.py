from selenium.webdriver.common.by import By


class BaseLocators:
# Кнопка входа на главной
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[contains(., 'Войти в аккаунт')]")
# Поле email
    EMAIL_FIELD = (By.XPATH, "//input[@type='text']")
# Поле пароля
    PASS_FIELD = (By.XPATH, "//input[@type='password']")
# Кнопка - Войти
    LOGIN_BUTTON = (By.XPATH, "//button[contains(., 'Войти')]")

# Кнопка - Конструктор
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
# Кнопка - Лента заказов
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")

# Контейнер конструктора
    BURGER_CONSTRUCTOR = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket__list__l9dp_')]")
# Булка
    FLUOR_BUN = (By.XPATH, '//img[@alt="Флюоресцентная булка R2-D3"]')
# Булка - ингредиент
    INGREDIENT_BUN = (By.XPATH, "//img[contains(@alt, 'Флюоресцентная булка R2-D3')]")
# Соус - ингредиент
    INGREDIENT_SOUCE = (By.XPATH, "//img[contains(@alt, 'Соус Spicy-X')]")

# Заголовок ленты
    TITLE_FEED = (By.XPATH, "//h1[@class='text text_type_main-large mt-10 mb-5' and text()='Лента заказов']")
# Модальное окно
    MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal')]")
# Крестик закрытия
    MODAL_CLOSE = (By.XPATH, '//button[contains(@class, "Modal_modal__close")]')
# Счётчик соуса
    INGREDIENT_COUNTER = (By.XPATH, "//p[text()='Соус Spicy-X']/ancestor::a//p[contains(@class, 'counter_counter__num')]")