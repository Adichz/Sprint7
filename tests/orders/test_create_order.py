import allure
import json
import pytest
from conftest import courier


from data import ORDER_DATA_1, ORDER_DATA_2, ORDER_DATA_3, ORDER_DATA_4
from methods.order_methods import OrderMethods

@allure.description('Класс тестирования заказов.')
class TestCreateOrder:

    @allure.step('Создаем заказы с разными цветами,с двумя цветами, без цветов. Ожидаем ответ = 201, и получение Track ')
    @pytest.mark.parametrize("order_data", [ORDER_DATA_1, ORDER_DATA_2, ORDER_DATA_3, ORDER_DATA_4])
    def test_create_order(self, order_data):
        new_order = OrderMethods.create_order(json.dumps(order_data))
        print(new_order.json()['track'])
        assert new_order.status_code == 201 and new_order.json()['track'] is not None

    @allure.step('Создаем курьера, заказ, проверяем что возвращется список заказов, удаляем курьера.')
    def test_check_order(self, courier):
        response = OrderMethods.check_order(courier)
        assert response is not None