
BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1/'
ORDERS_URL = 'orders'
COURIERS_URL = 'courier'

import random
import string


def gen_payload():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    return payload

ORDER_DATA_1 = {
    "firstName": "Юра",
    "lastName": "Фикстура",
    "address": "Тестировочная 25, кв1",
    "metroStation": "Домодедово",
    "phone": "+7 950 505 05 05",
    "rentTime": 1,
    "deliveryDate": "2024-01-01",
    "comment": "first",
    "color": ["GREY"]
}


ORDER_DATA_2 = {
    "firstName": "Рома",
    "lastName": "Папилома",
    "address": "Тестировочная 13, кв666",
    "metroStation": "Шереметьево",
    "phone": "+7 950 666 13 13",
    "rentTime": 2,
    "deliveryDate": "2024-02-02",
    "comment": "second",
    "color": ["BLACK"]
}


ORDER_DATA_3 = {
    "firstName": "Витек",
    "lastName": "Отек",
    "address": "Програмиссткая 1",
    "metroStation": "Пулково",
    "phone": "+7 950 555 55 55",
    "rentTime": 3,
    "deliveryDate": "2024-03-03",
    "comment": "third",
    "color": ["BLACK", "GREY"]
}


ORDER_DATA_4 = {
    "firstName": "Толик",
    "lastName": "Алкоголик",
    "address": "Сатана, последний круг",
    "metroStation": "Кочпон, три колодца",
    "phone": "+7 950 555 55 55",
    "rentTime": 4,
    "deliveryDate": "2024-04-204",
    "comment": "fourth",
    "color": []
}


