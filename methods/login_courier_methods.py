import requests
from data import BASE_URL, COURIERS_URL, gen_payload


def create_courier(payload):
    requests.post(f'{BASE_URL}{COURIERS_URL}', data=payload)


class LoginCourierMethods:
    @staticmethod
    def login_courier():
        payload = gen_payload()
        create_courier(payload)
        return requests.post(f'{BASE_URL}{COURIERS_URL}/login', data={'login': payload.get('login'), 'password': payload.get('password')})

    @staticmethod
    def login_courier_no_login():
        payload = gen_payload()
        create_courier(payload)
        return requests.post(f'{BASE_URL}{COURIERS_URL}/login', data={'password': payload.get('password')})

    @staticmethod
    def login_courier_with_wrong_password():
        payload = gen_payload()
        create_courier(payload)
        return requests.post(f'{BASE_URL}{COURIERS_URL}/login', data={'login': payload.get('login'), 'password': 'parrol'})

    @staticmethod
    def login_courier_incognito():
        payload = gen_payload()
        return requests.post(f'{BASE_URL}{COURIERS_URL}/login', data={'login': payload.get('login'), 'password': payload.get('password')})