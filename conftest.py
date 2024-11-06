import pytest

from methods.courier_methods import CourierMethods
from precondition.precondition_for_courier import data_courier,data_authorization_courier

@pytest.fixture()
def create_courier_and_login_data():
    courier_methods = CourierMethods()
    login_data = data_courier()
    courier_methods.create_courier(login_data)
    response = courier_methods.authorization_courier(login_data)
    yield login_data
    courier_methods.delete_courier(response.json()['id'])