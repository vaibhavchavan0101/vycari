from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

import copy

class SignUpTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('register_user')
        self.data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'Password123!',
            'phone': '7890324321',
            'bio': 'test',
            'gender': 'M',
            'country': 'indian'
        }

    def test_sign_up_for_valid_data(self):
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_sign_up_for_username_missing(self):
        data = copy.deepcopy(self.data)
        data['username'] = ' '
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_sign_up_for_invalid_email(self):
        data = copy.deepcopy(self.data)
        data['email'] = 'test@com'
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_sign_up_for_invalid_phone(self):
        data = copy.deepcopy(self.data)
        data['phone'] = '1234567890'
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_sign_up_for_missing_upper_case_char_in_password(self):
        data = copy.deepcopy(self.data)
        data['password'] = 'assword123!'
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_sign_up_for_missing_lower_case_char_in_password(self):
        data = copy.deepcopy(self.data)
        data['password'] = 'PASSWORD123!'
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_sign_up_for_missing_numeric_value_in_password(self):
        data = copy.deepcopy(self.data)
        data['password'] = 'Password!'
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_sign_up_for_missing_special_char_in_password(self):
        data = copy.deepcopy(self.data)
        data['password'] = 'assword123'
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class UserAuthenticationTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('login')
        self.register_url = reverse('register_user')
        self.data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'Password123!',
            'phone': '7890324321',
            'bio': 'test',
            'gender': 'M',
            'country': 'indian'
        }
        self.client.post(self.register_url, self.data)

    def test_user_authentication_with_username(self):
        response = self.client.post(self.url, {'username': self.data['username'], 'password': self.data['password']})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_authentication_with_invalid_username(self):
        data = copy.deepcopy(self.data)
        data['username'] = 'test'
        response = self.client.post(self.url, {'username': data['username'], 'password': self.data['password']})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_user_authentication_with_email(self):
        response = self.client.post(self.url, {'username': self.data['email'], 'password': self.data['password']})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_user_authentication_with_invalid_email(self):
        data = copy.deepcopy(self.data)
        data['email'] = 'testtest@example.com'
        response = self.client.post(self.url, {'username': data['email'], 'password': self.data['password']})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_user_authentication_with_phone(self):
        response = self.client.post(self.url, {'username': self.data['phone'], 'password': self.data['password']})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_user_authentication_with_invalid_phone(self):
        data = copy.deepcopy(self.data)
        data['phone'] = '7890324222'
        response = self.client.post(self.url, {'username': data['phone'], 'password': self.data['password']})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
