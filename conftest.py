import pytest
import json

from data import gen_payload, ORDER_DATA_1
from methods.courier_methods import CourierMethods
from methods.order_methods import OrderMethods


@pytest.fixture()
def courier():
    payload = gen_payload()
    CourierMethods.create_courier(payload)
    courier_id = CourierMethods.get_courier_id(payload.get('login'), payload.get('password'))
    order_response = OrderMethods().create_order(json.dumps(ORDER_DATA_1))
    order_id = OrderMethods.get_order_id(order_response.json()["track"])
    OrderMethods.accept_order(order_id, courier_id)
    yield courier_id
    CourierMethods().delete_courier(courier_id)