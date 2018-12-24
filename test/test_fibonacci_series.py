from unittest import TestCase
from  fibonacci_series import fibonacci_ser


class TestFibonacciSeries(TestCase):

    def test_fibonacci_ser_for_success(self):
        ip = 9
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21]
        result = fibonacci_ser(ip)
        self.assertEqual(expected, result)

    def test_fibonacci_ser_for_empty_string_or_string(self):
        # empty string input
        ip = ""
        expected = "Invalid input"
        result = fibonacci_ser(ip)
        self.assertEqual(expected, result)

        # string input
        ip = "aish"
        expected = "Invalid input"
        result = fibonacci_ser(ip)
        self.assertEqual(expected, result)

    def test_fibonacci_fixed_ser_for_None(self):
        ip = None
        expected = None
        result = fibonacci_ser(ip)
        self.assertEqual(expected, result)