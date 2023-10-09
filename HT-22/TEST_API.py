"""HomeTask_22.
https://qauto.forstudy.space/api-docs/
Написати п'ять тестів що проходять через пункти
1. Реєстрація користувача
2. Створення машини POST cars
3. редагування машини
4. отримання даних через GET в Cars або Expenses
5. Видалення користувача
"""


import requests
import pytest
import json


from Hillel_api import s, auth, users, cars, expenses


def test_user_signup():
    user_data = {
        "name": "Margo",
        "lastName": "Test",
        "email": "testMargo@test.com",
        "password": "Qwerty12345",
        "repeatPassword": "Qwerty12345"
    }
    r = auth.signup(s, user_data)
    r_json = r.json()
    assert r.status_code == 201, f'Wrong status code:\n{r_json}'
    assert r_json.get('status', False) == "ok", "Key 'status' is not ok"


def test_signin():
    user_data = {
         "email": "testMargo@test.com",
         "password": "Qwerty12345",
         "remember": False
    }
    r = auth.signin(s, user_data)
    r_json = r.json()
    assert r.status_code == 200, f"Wrong status code:\n{r_json}"
    assert r_json.get('status', False) == "ok", "Key 'status' is not ok"


def test_cars_created():
    user_data = {
        "carBrandId": 1,
        "carModelId": 1,
        "mileage": 124
    }
    r = cars.cars_post(s, user_data)
    r_json = r.json()
    print(r_json)
    assert r.status_code == 201, f"Wrong status code:\n{r_json}"
    assert r_json.get('status', False) == "ok", "Key 'status' is not ok"
    print(r_json)


def test_cars_id_edits():
    user_data = {
         "carBrandId": 1,
         "carModelId": 1,
         "mileage": 168223
    }
    r = cars.cars_id_put(s, user_data)
    r_json = r.json()
    assert r.status_code == 404, f"Expected status code 404, but got {r.status_code}"
    assert r_json.get('status', '') == "error", "Expected 'status' to be 'error'"
    assert r_json.get('message', '') == "Car not found", "Expected 'message' to be 'Car not found'"


def test_cars_get_models():
    r = cars.models(s)
    r_json = r.json()
    assert r.status_code == 200, f"Wrong status code:\n{r_json}"
    assert r_json.get('status', False) == "ok", "Key 'status' is not ok"


def test_expenses_get():
    request_body = {}
    r = expenses.expenses_get(s, request_body)
    r_json = r.json()
    assert r.status_code == 200, f"Wrong status code:\n{r_json}"
    assert r_json.get('status', False) == "ok", "Key 'status' is not ok"


def test_users_delete():
        r = users.users(s)
        r_json = r.json()
        assert r.status_code == 200, f"Wrong status code:\n{r_json}"
        assert r_json.get('status', False) == "ok", "Key 'status' is not ok"
