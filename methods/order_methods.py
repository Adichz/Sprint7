import allure
import requests
from data import BASE_URL, ORDERS_URL

@allure.title('Методы создания заказа.')
class OrderMethods:

    @staticmethod
    @allure.step('Создание заказа')
    def create_order(payload):
        return requests.post(f'{BASE_URL}{ORDERS_URL}', data = payload)

    @staticmethod
    @allure.step('Получение "Track"')
    def get_order_id(track):
        response = requests.get(f'{BASE_URL}{ORDERS_URL}/track?t={track}')
        return response.json()["order"]["id"]

    @staticmethod
    @allure.step('Принимаем заказ')
    def accept_order(order_id, courier_id):
        return requests.put(f'{BASE_URL}{ORDERS_URL}/accept/{order_id}?courierId={courier_id}')

    @staticmethod
    @allure.step('Проверка заказа')
    def check_order(courier):
        return requests.get(f'{BASE_URL}/{ORDERS_URL}?courierId={courier}')