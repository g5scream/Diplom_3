import pytest
import requests
import allure
from selenium import webdriver
from helpers.urls_api import Urls
from helpers.urls_api import UrlApi, generate_user, delete_user
from pages.base_page import BasePage
from locators.base_locators import BaseLocators


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default= None,                                           # None запускаем оба браузера
        help="Browser to run tests: chrome or firefox"
    )

@pytest.fixture(params=["chrome", "firefox"])
def browser_name(request):
    desired_browser = request.config.getoption("--browser")
    if desired_browser and request.param != desired_browser:
        pytest.skip(f"Пропуск {request.param} (запускаем {desired_browser})")
    return request.param

@pytest.fixture
def browser(browser_name):
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def created_user():
    user_data = generate_user(password_length=6)
    with allure.step("Создание тестового пользователя"):
        response = requests.post(f'{UrlApi.CREATE_USER}', json=user_data)
    
        created_user = response.json()
        created_user['id'] = created_user.get('id')
        created_user['email'] = user_data['email']  
        created_user['password'] = user_data['password']  

    yield created_user
    token = created_user.get("accessToken")
    if token:
        with allure.step("Удаление тестового пользователя"):
            delete_response = delete_user(token)
            with allure.step(f"Проверка статуса удаления: {delete_response.status_code}"):
                assert delete_response.status_code == 202, \
                    f"Ожидался статус 202, но получен {delete_response.status_code}"

@pytest.fixture
def logged_in_browser(browser, created_user):
    browser.get(Urls.BASE_URL)
    base_page = BasePage(browser)
    base_page.login(created_user["email"], created_user["password"])
    base_page.wait_for_element_visible(BaseLocators.INGREDIENT_BUN)
    return browser
