from data import BASE_URL, COURIERS_URL, gen_payload
import requests


class CourierMethods:
    @staticmethod
    def create_courier(payload):
        response = requests.post(f'{BASE_URL}{COURIERS_URL}', data=payload)
        return response

    @staticmethod
    def create_courier_no_login():
        payload = gen_payload()
        response = requests.post(f'{BASE_URL}{COURIERS_URL}',
                             data={'password': payload.get('password'), 'firstName': payload.get('first_name')})
        return response

    @staticmethod
    def create_courier_no_pwd():
        payload = gen_payload()
        response = requests.post(f'{BASE_URL}{COURIERS_URL}',
                             data={'login': payload.get('login'), 'firstName': payload.get('first_name')})
        return response

    @staticmethod
    def create_courier_two_times():
        payload = gen_payload()
        requests.post(f'{BASE_URL}{COURIERS_URL}', data=payload)
        return requests.post(f'{BASE_URL}{COURIERS_URL}', data=payload)

    @staticmethod
    def login_courier(login, password):
        response = requests.post(f'{BASE_URL}{COURIERS_URL}/login', data={'login': login, 'password': password})
        return response.json()['id']

    @staticmethod
    def delete_courier(id):
        requests.delete(f'{BASE_URL}{COURIERS_URL}/{id}')