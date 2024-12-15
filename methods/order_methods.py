import requests
from data import BASE_URL, ORDERS_URL


class OrderMethods:
    @staticmethod
    def create_order(payload):
        return requests.post(f'{BASE_URL}{ORDERS_URL}', data = payload)

    @staticmethod
    def get_order_id(track):
        response = requests.get(f'{BASE_URL}{ORDERS_URL}/track?t={track}')
        return response.json()["order"]["id"]

    @staticmethod
    def accept_order(order_id, courier_id):
        return requests.put(f'{BASE_URL}{ORDERS_URL}/accept/{order_id}?courierId={courier_id}')

    @staticmethod
    def check_order(courier):
        return requests.get(f'{BASE_URL}/{ORDERS_URL}?courierId={courier}')