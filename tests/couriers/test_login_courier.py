import allure
from methods.login_courier_methods import LoginCourierMethods

@allure.title('Класс тестирования создания курьера.')
class TestLoginCourier:

    @allure.step('Логинимся курьером. Ожидаем ответ = 200, и получение id')
    def test_login_courier(self):
        login_courier = LoginCourierMethods.login_courier()
        assert login_courier.status_code == 200 and login_courier.json()['id'] is not None

    @allure.step('Логинимся курьером без логина. Ожидаем ответ = 400, и получение сообщения об ошибке')
    def test_login_courier_no_login(self):
        login_courier = LoginCourierMethods.login_courier_no_login()
        assert login_courier.status_code == 400 and login_courier.json()['message'] == 'Недостаточно данных для входа'

    @allure.step('Логинимся курьером с неправильным паролем. Ожидаем ответ = 404, и получение сообщения об ошибке')
    def test_login_courier_with_wrong_password(self):
        login_courier = LoginCourierMethods.login_courier_with_wrong_password()
        assert login_courier.status_code == 404 and login_courier.json()['message'] == 'Учетная запись не найдена'

    @allure.step('Логинимся несуществующим курьером . Ожидаем ответ = 404, и получение сообщения об ошибке')
    def test_login_courier_incognito(self):
        login_courier = LoginCourierMethods.login_courier_incognito()
        assert login_courier.status_code == 404 and login_courier.json()['message'] == 'Учетная запись не найдена'