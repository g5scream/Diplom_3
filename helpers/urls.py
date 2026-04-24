from urllib.parse import urljoin

class Urls:
    BASE_URL = 'https://stellarburgers.education-services.ru'

    FEED_URL = urljoin(BASE_URL, '/feed')
    CREATE_USER = urljoin(BASE_URL, '/api/auth/register')
    DELETE_USER = urljoin(BASE_URL, '/api/auth/user')