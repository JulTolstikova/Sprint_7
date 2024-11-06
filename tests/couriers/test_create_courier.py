import allure

from data import delete_field
from methods.courier_methods import CourierMethods
from precondition.precondition_for_courier import data_courier


class TestCreateCouriers:
    @allure.title('Успешное создание курьера')
    def test_create_courier_successful(self):
        courier_methods = CourierMethods()
        status_code, current_response = courier_methods.create_courier(data_courier())
        assert status_code == 201 and current_response == {'ok': True}

    @allure.title('Создание двух одинаковых курьеров')
    def test_create_duplicate_courier(self):
        courier_methods = CourierMethods()
        first_courier = data_courier()
        courier_methods.create_courier(first_courier)
        status_code, current_response = courier_methods.create_courier(first_courier)
        assert status_code == 409 and current_response == {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}

    @allure.title('Создание курьера без логина')
    def test_create_courier_without_login(self):
        courier_methods = CourierMethods()
        request_without_login = delete_field(data_courier(), "login")
        status_code, current_response = courier_methods.create_courier(request_without_login)
        assert status_code == 400 and current_response == {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}