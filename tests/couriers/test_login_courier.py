import allure

from conftest import create_courier_and_login_data
from methods.courier_methods import CourierMethods
from data import delete_field, NOT_EXISTENCE_USER
from precondition.precondition_for_courier import data_authorization_courier

class TestAuthorizationCouriers:

    @allure.title('Успешная авторизация курьера')
    def test_authorization_courier_successful(self, create_courier_and_login_data):
        courier_methods = CourierMethods()
        response = courier_methods.authorization_courier(
            data_authorization_courier(create_courier_and_login_data)
        )
        assert response.status_code == 200 and response.json()['id']

    @allure.title('Авторизация с некорректным паролем')
    def test_authorization_courier_with_invalid_password(self, create_courier_and_login_data):
        courier_methods = CourierMethods()
        create_courier_and_login_data['password'] = 'test_password'
        response = courier_methods.authorization_courier(create_courier_and_login_data)
        assert response.status_code == 404 and response.json() == {'code': 404, "message": "Учетная запись не найдена"}

    @allure.title('Авторизация под несуществующим курьером')
    def test_authorization_unknown_courier(self):
        courier_methods = CourierMethods()
        response = courier_methods.authorization_courier(NOT_EXISTENCE_USER)
        assert response.status_code == 404 and response.json() == {'code': 404, "message": "Учетная запись не найдена"}

    @allure.title('Авторизация без логина')
    def test_authorization_no_login_courier(self, create_courier_and_login_data):
        courier_methods = CourierMethods()
        request_without_login = delete_field(create_courier_and_login_data, "login")
        response = courier_methods.authorization_courier(request_without_login)
        assert response.status_code == 400 and response.json() == {'code': 400, 'message': 'Недостаточно данных для входа'}

    @allure.title('Авторизация без пароля')
    def test_authorization_courier_with_no_password(self, create_courier_and_login_data):
        courier_methods = CourierMethods()
        create_courier_and_login_data['password'] = ''
        response = courier_methods.authorization_courier(create_courier_and_login_data)
        assert response.status_code == 400 and response.json() == {'code': 400,
                                                                   'message': 'Недостаточно данных для входа'}