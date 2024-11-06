import allure
import requests

from data import BASE_URL, COURIER_URL


class CourierMethods:

    @allure.step('Cоздать курьера')
    def create_courier(self, params):
        response = requests.post(f"{BASE_URL}{COURIER_URL}", json=params)
        return response.status_code, response.json()

    @allure.step('Авторизовать курьера')
    def authorization_courier(self, params):
        response = requests.post(f"{BASE_URL}{COURIER_URL}login", json=params)
        return response

    @allure.step('Удалить курьера')
    def delete_courier(self, id):
        response = requests.delete(f"{BASE_URL}{COURIER_URL}{id}")
        return response.status_code, response.json()