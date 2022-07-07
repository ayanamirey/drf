from django.test import TestCase
from women.logic import operations


class LogicTestCase(TestCase):
    def setUp(self):
        pass

    def test_plus(self):
        result = operations(6, 13, '+')
        self.assertEqual(19, result)

    def test_minus(self):
        result = operations(7, 3, '-')
        self.assertEqual(4, result)

    def test_multiply(self):
        result = operations(5, 3, '*')
        self.assertEqual(15, result)

