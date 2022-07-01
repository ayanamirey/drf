from datetime import time

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from women.models import Women, Category


# title
# content
# time_create
# time_update
# is_published
# cat
# user

class WomenTests(APITestCase):
    def setUp(self):
        Women.objects.create(title='Дора', content='Дора контент')
        Women.objects.create(title='Бейонсе', content='Бейонсе контент')

    def test_women_list(self):
        url = reverse('women-list')
        response = self.client.get(url)
        # self.assertEqual(response.data, {'id': 1, 'title':'Дора'})
        self.assertTrue( {'id': 1, 'title':'Дора'} in response.data)

        # url = reverse('account-list')
        # data = {'name': 'DabApps'}
        # response = self.client.post(url, data, format='json')
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # self.assertEqual(Account.objects.count(), 1)
        # self.assertEqual(Account.objects.get().name, 'DabApps')
