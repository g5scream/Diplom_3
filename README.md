# Diplom_3
Автотесты для UI

## Стек технологий
* **Язык:** Python 3.14;
* **Фреймворк:** PyTest
* **UI‑тестирование:** Selenium WebDriver
* **Паттерн проектирования:** Page Object
* **HTTP‑клиент для API‑запросов:** requests
* **Генерация тестовых данных:** Faker
* **Отчётность:** Allure

## Структура проекта

    Diplom_3/
        ├── allure-results/         # Результаты Allure
        ├── helpers/                # Вспомогательные модули
        │   ├── urls_api.py         # API‑URL и функции работы с API
        │   └── urls.py             # Базовые URL веб‑интерфейса
        ├── locators/               # Локаторы элементов
        │   ├── base_locators.py    # Общие локаторы
        │   └── order_locators.py   # Локаторы для ленты заказов
        ├── pages/                  # Классы страниц (реализация паттерна Page Object)
        │   ├── base_page.py        # Базовый класс страницы
        │   ├── main_page.py        # Главная страница
        │   └── order_page.py       # Страница заказа
        ├── tests/                  # Тесты
        │   ├── test_main_page.py   # Тесты главной страницы
        │   └── test_order_page.py  # Тесты ленты заказов
        ├── conftest.py             # Фикстуры pytest
        ├── requirements.txt        # Зависимости
        └── README.md               # Эта документация

## Назначение ключевых компонентов
**conftest.py** — фикстуры: запуск браузера (Chrome/Firefox), создание/удаление тестового пользователя, авторизация.

**helpers/** — утилиты: генерация тестовых пользователей, API‑запросы, URL.

**locators/** — XPath/CSS‑локаторы элементов интерфейса.

**pages/** — классы страниц с методами взаимодействия с элементами интерфейса. Реализован паттерн Page Object.

**tests/** — тестовые сценарии для главной страницы и ленты заказов.

**allure-results/** — папка для генерации отчётов Allure.

**requirements.txt** — список зависимостей для установки.

## Запуск тестов и покрытие (pytest‑cov)

Все тесты в обоих браузерах: `pytest`

Только в Chrome: `pytest --browser chrome`

Только в Firefox: `pytest --browser firefox`

С генерацией отчёта Allure: `pytest --alluredir=allure-results`

Для просмотра отчёта выполните: `allure serve allure-results`

С измерением покрытия кода (100 %): `pytest --cov=. --cov-report=html`

После выполнения откроется отчёт в папке htmlcov/index.html