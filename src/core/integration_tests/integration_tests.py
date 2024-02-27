from django.test.runner import DiscoverRunner
from django.test import TestCase, RequestFactory

from user.views import RegisterUserView


class NoDbTestRunner(TestCase, DiscoverRunner):
    """ A test runner to test without database creation """

    def setUp(self):
        self.factory = RequestFactory()

    def setup_databases(self, **kwargs):
        """ Override the database creation defined in parent class """
        pass

    def teardown_databases(self, old_config, **kwargs):
        """ Override the database teardown defined in parent class """
        pass

    def test_create_user(self, **kwargs):
        BASE_URL = 'http://localhost:8000/api/user/register/'
        payload = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'Password123!',
            'phone': '7890324321',
            'bio': 'test',
            'gender': 'M',
            'country': 'indian'
        }

        request = self.factory.post(BASE_URL, data=payload)
        response = RegisterUserView.as_view({'post': 'create'})(request)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['username'], payload['username'])
        self.assertEqual(response.data['email'], payload['email'])
        self.assertEqual(response.data['phone'], payload['phone'])
        self.assertEqual(response.data['bio'], payload['bio'])
        self.assertEqual(response.data['gender'], payload['gender'])
        self.assertEqual(response.data['country'], payload['country'])
