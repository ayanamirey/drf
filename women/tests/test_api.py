from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

from women.models import Women
from women.serializers import WomenSerializer


class WomenApiTestCase(APITestCase):
    def setUp(self):
        test_user1 = User.objects.create_user(username='testuser1', password='12345')
        Women.objects.create(title='Дора', content='Дора контент', user=test_user1)
        Women.objects.create(title='Дора 2', content='Дора 2 контент', user=test_user1)

    def test_get(self):
        womens = Women.objects.all()
        response = self.client.get(reverse('women_list'))
        serializer_data = WomenSerializer(womens, many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
