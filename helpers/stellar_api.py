from uuid import uuid4

import allure
import requests

from config import BASE_URL


class StellarApi:
    def __init__(self):
        self.session = requests.Session()

    @allure.step('Создать тестового пользователя через API')
    def create_user(self):
        data = {'email': f'valeriia_ui_{uuid4().hex}@example.com',
                'password': f'Password_{uuid4().hex}', 'name': 'Valeriia'}
        response = self.session.post(BASE_URL + '/api/auth/register', json=data, timeout=30)
        response.raise_for_status()
        self.session.headers['Authorization'] = response.json()['accessToken']
        return data

    @allure.step('Создать заказ для подготовки теста через API')
    def create_order(self):
        response = self.session.get(BASE_URL + '/api/ingredients', timeout=30)
        response.raise_for_status()
        ingredients = response.json()['data']
        bun = next(item['_id'] for item in ingredients if item['type'] == 'bun')
        filling = next(item['_id'] for item in ingredients if item['type'] == 'main')
        order = self.session.post(BASE_URL + '/api/orders',
                                  json={'ingredients': [bun, filling, bun]}, timeout=40)
        order.raise_for_status()
        return order.json()['order']['number']

    @allure.step('Удалить тестового пользователя через API')
    def delete_user(self):
        self.session.delete(BASE_URL + '/api/auth/user', timeout=30).raise_for_status()

    def close(self):
        self.session.close()
