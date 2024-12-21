import allure

from data import gen_payload
from methods.courier_methods import CourierMethods


@allure.feature('Класс тестирования создания курьера.')
class TestCreateCourier:

    @allure.title('Создаем курьера с заполнением всех данных. Ожидаем ответ = 201, ok,True')
    def test_create_courier(self):
        payload = gen_payload()
        new_courier = CourierMethods.create_courier(payload)
        assert new_courier.status_code == 201 and new_courier.json() == {'ok': True}

    @allure.title('Создаем курьера 2 раза. Ожидаем ответ = 409 и сообщение что Логин уже используется')
    def test_create_courier_two_times(self):
        the_same_courier = CourierMethods.create_courier_two_times()
        assert the_same_courier.status_code == 409 and the_same_courier.json()['message'] == 'Этот логин уже используется. Попробуйте другой.'

    @allure.title('Создаем курьера без Логина. Ожидаем ответ = 400 и сообщение что данных недостаточно')
    def test_create_courier_no_login(self):
        courier_no_login = CourierMethods.create_courier_no_login()
        assert courier_no_login.status_code == 400 and courier_no_login.json()['message'] == 'Недостаточно данных для создания учетной записи'

    @allure.title('Создаем курьера без Пароля. Ожидаем ответ = 400 и сообщение что данных недостаточно')
    def test_create_courier_no_pwd(self):
        courier_no_pwd = CourierMethods.create_courier_no_pwd()
        assert courier_no_pwd.status_code == 400 and courier_no_pwd.json()['message'] == 'Недостаточно данных для создания учетной записи'


