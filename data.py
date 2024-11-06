import random
import string

BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1/'
COURIER_URL = 'courier/'
ORDERS_URL = 'orders/'

def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def delete_field(payload, field):
    payload.pop(field)
    return payload

NOT_EXISTENCE_USER = {
    'login': 'Gregor',
    'password': 'Zamza'
}

ORDER_DATA_GREY = {
    "firstName": "Eren",
    "lastName": "Yeger",
    "address": "Konoha, 142 apt.",
    "metroStation": 2,
    "phone": "+7 800 355 35 77",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "test_comment",
    "color": [
        "GREY"
    ]
}

ORDER_DATA_BLACK = {
    "firstName": "Mikasa",
    "lastName": "Akkerman",
    "address": "Konoha, 142 apt.",
    "metroStation": 2,
    "phone": "+7 800 355 35 55",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "test_comment_2",
    "color": [
        "BLACK"
    ]
}

ORDER_DATA_BLACK_GREY = {
    "firstName": "Armin",
    "lastName": "Arlert",
    "address": "Konoha, 142 apt.",
    "metroStation": 3,
    "phone": "+7 800 355 35 88",
    "rentTime": 2,
    "deliveryDate": "2020-06-06",
    "comment": "test_comment_3",
    "color": [
        "BLACK",
        "GREY"
    ]
}

ORDER_DATA_WITHOUT_COLOR = {
    "firstName": "Sasha",
    "lastName": "Brown",
    "address": "Konoha, 142 apt.",
    "metroStation": 7,
    "phone": "+7 800 355 35 88",
    "rentTime": 4,
    "deliveryDate": "2020-06-06",
    "comment": "test_comment_4",
}
