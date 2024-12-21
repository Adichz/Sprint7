import requests
import allure
from data import BASE_URL, COURIERS_URL, gen_payload
from methods.courier_methods import CourierMethods

@allure.title('Методы Логина курьера.')
class LoginCourierMethods:

    @staticmethod
    @allure.step('Логинимся курьером')
    def login_courier():
        payload = gen_payload()
        CourierMethods.create_courier(payload)
        return requests.post(f'{BASE_URL}{COURIERS_URL}/login', data={'login': payload.get('login'), 'password': payload.get('password')})

    @staticmethod
    @allure.step('Логинимся курьером без логина')
    def login_courier_no_login():
        payload = gen_payload()
        CourierMethods.create_courier(payload)
        return requests.post(f'{BASE_URL}{COURIERS_URL}/login', data={'password': payload.get('password')})

    @staticmethod
    @allure.step('Логинимся курьером с неверным паролем')
    def login_courier_with_wrong_password():
        payload = gen_payload()
        CourierMethods.create_courier(payload)
        return requests.post(f'{BASE_URL}{COURIERS_URL}/login', data={'login': payload.get('login'), 'password': 'parrol'})

    @staticmethod
    @allure.step('Логинимся курьером под несуществующим пользоваателем')
    def login_courier_incognito():
        payload = gen_payload()
        return requests.post(f'{BASE_URL}{COURIERS_URL}/login', data={'login': payload.get('login'), 'password': payload.get('password')})