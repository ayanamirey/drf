from django.test import TestCase
import datetime
from django.db import models
from django.urls import reverse

from women.models import Women
from django.contrib.auth.models import User

from women.serializers import WomenSerializer


class WomenSerializerTestCase(TestCase):
    def test_ok(self):
        test_user1 = User.objects.create_user(username='testuser1', password='12345')
        Women.objects.create(title='Дора', content='Дора контент', user=test_user1)
        Women.objects.create(title='Дора 2', content='Дора 2 контент', user=test_user1)
        womens = Women.objects.all()
        data = WomenSerializer(womens, many=True).data
        time_test = datetime.datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S")
        expected_data = [
            {
                'id': womens[0].id,
                'title': 'Дора',
                'content': 'Дора контент',
                'time_create': time_test,
                'time_update': time_test,
                'is_published': True,
                'cat': None,
            },
            {
                'id': womens[1].id,
                'title': 'Дора 2',
                'content': 'Дора 2 контент',
                'time_create': time_test,
                'time_update': time_test,
                'is_published': True,
                'cat': None,
            }
        ]
        self.assertEqual(expected_data, data)
