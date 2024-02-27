from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

import copy

user_data = {
    'username': 'testuser',
    'email': 'test@example.com',
    'password': 'Password123!',
    'phone': '7890324321',
    'bio': 'test',
    'gender': 'M',
    'country': 'indian'
}

class SignUpTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('register-list')

    def test_sign_up_for_valid_data(self):
        response = self.client.post(self.url, user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_sign_up_for_username_missing(self):
        data = copy.deepcopy(user_data)
        data['username'] = ' '
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_sign_up_for_invalid_email(self):
        data = copy.deepcopy(user_data)
        data['email'] = 'test@com'
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_sign_up_for_invalid_phone(self):
        data = copy.deepcopy(user_data)
        data['phone'] = '1234567890'
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_sign_up_for_missing_bio(self):
        data = copy.deepcopy(user_data)
        data['bio'] = ' '
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_sign_up_for_missing_gender(self):
        data = copy.deepcopy(user_data)
        data['gender'] = ' '
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_sign_up_for_all_numeric_value_in_password(self):
        data = copy.deepcopy(user_data)
        data['password'] = '123456789'
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_sign_up_for_missing_country(self):
        data = copy.deepcopy(user_data)
        data['country'] = ' '
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class UserAuthenticationTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('login')
        self.register_url = reverse('register-list')

        self.client.post(self.register_url, user_data)

    def test_user_authentication_with_username(self):
        response = self.client.post(self.url, {'username': user_data['username'], 'password': user_data['password']})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_authentication_with_invalid_username(self):
        data = copy.deepcopy(user_data)
        data['username'] = 'test'
        response = self.client.post(self.url, {'username': data['username'], 'password': data['password']})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_authentication_with_email(self):
        response = self.client.post(self.url, {'username': user_data['email'], 'password': user_data['password']})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_authentication_with_invalid_email(self):
        data = copy.deepcopy(user_data)
        data['email'] = 'testtest@example.com'
        response = self.client.post(self.url, {'username': data['email'], 'password': data['password']})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_authentication_with_phone(self):
        response = self.client.post(self.url, {'username': user_data['phone'], 'password': user_data['password']})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_authentication_with_invalid_phone(self):
        data = copy.deepcopy(user_data)
        data['phone'] = '7890324222'
        response = self.client.post(self.url, {'username': data['phone'], 'password': data['password']})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
