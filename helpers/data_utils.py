import requests
from faker import Faker
from helpers.urls import Urls

fake = Faker('en_US')

def generate_user(is_random=False, password_length=6):
    email_fmt = f"{fake.user_name()}.{fake.random_number(digits=6)}@yandex.ru"
    password = fake.password(
        length=password_length,
        special_chars=True,
        digits=True,
        upper_case=True,
        lower_case=True
    )
    return {
        "email": email_fmt,
        "password": password,
        "name": fake.first_name()
    }

def _get_auth_headers(access_token):
    return {"Authorization": access_token} if access_token else {}

def delete_user( access_token):
    headers = _get_auth_headers(access_token)
    return requests.delete(Urls.DELETE_USER, headers=headers)
