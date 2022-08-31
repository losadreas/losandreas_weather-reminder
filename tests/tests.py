from django.urls import reverse
from rest_framework.test import RequestsClient, APITestCase
from django.test import Client
from rest_framework import status

client_request = RequestsClient()


class AccountTests(APITestCase):
    def setUp(self):
        url = reverse('register')
        c = Client()
        c.post(url, {'username': 'test01',
                                'email': 'test01@test.tu',
                                'password1': '(1234567890)',
                                'password2': '(1234567890)'
                                })

    def test_create_account(self):
        url = '/api/token/'
        data = {
            "email": "test01@test.tu",
            "password": "(1234567890)"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_token(self):
        url = '/api/token/'
        data = {
            "email": "test01@test.tu",
            "password": "(1234567890)"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ApiTests(APITestCase):
    token = None

    def setUp(self):
        url = reverse('register')
        c = Client()
        c.post(url, {'username': 'test01',
                                'email': 'test01@test.tu',
                                'password1': '(1234567890)',
                                'password2': '(1234567890)'
                                })
        url = '/api/token/'
        data = {
            "email": "test01@test.tu",
            "password": "(1234567890)"
        }
        response = self.client.post(url, data, format='json')
        ApiTests.token = response.data

    def test_token_auth(self):
        url = 'http://testserver/api/forecast_list/'
        value = f'Bearer {ApiTests.token["access"]}'
        header = {'Authorization': value}
        client_request.headers.update(header)
        response = client_request.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post(self):
        url = 'http://testserver/api/forecast_list/'
        value = f'Bearer {ApiTests.token["access"]}'
        header = {'Authorization': value}
        client_request.headers.update(header)
        data = {'city': 'Vancouver', 'period': 6}
        response = client_request.post(url, data)
        self.assertEqual(response.json(), {'forecast :': {'city': 'Vancouver', 'period': 6}})

    def test_delete(self):
        url_create = 'http://testserver/api/forecast_list/'
        url_delete = 'http://testserver/api/forecast_list/1/'
        value = f'Bearer {ApiTests.token["access"]}'
        header = {'Authorization': value}
        client_request.headers.update(header)
        data = {'city': 'Vancouver', 'period': 6}
        response_01 = client_request.post(url_create, data)
        response = client_request.delete(url_delete)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


