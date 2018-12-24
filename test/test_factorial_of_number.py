from unittest import TestCase
from factorial_of_number import factorial_num


class TestFactorialOfNumber(TestCase):

    def test_factorial_num_for_success(self):
        ip = 5
        expected = 120
        result = factorial_num(ip)
        self.assortEqual(expected, result)


    def test_factorial_num_for_empty_string_or_string(self):
        #empty string input
        ip = ""
        expected = "Invalid input"
        result = factorial_num(ip)
        self.assertEqual(expected, result)

        #string input
        ip = "abhi"
        expected = "Invalid input"
        result = factorial_num(ip)
        self.assertEqual(expected, result)

    def test_factorial_num_for_None(self):
        ip = None
        expected = None
        result = factorial_num(ip)
        self.assortEqual(expected, result)