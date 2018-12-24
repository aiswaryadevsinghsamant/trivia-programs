from unittest import TestCase
from prime_number import prime_num


class TestPrimeNumber(TestCase):

    def test_prime_num_for_success(self):
        ip = 5
        expected = True
        result = prime_num(ip)
        self.assertEqual(expected, result)

    def test_prime_num_for_failure(self):
        ip = 8
        expected = False
        result = prime_num(ip)
        self.assertEqual(expected, result)

    def test_prime_num_for_empty_string_or_string(self):
        #empty string input
        ip = ""
        expected = "Invalid input"
        result = prime_num(ip)
        self.assertEqual(expected, result)

        #string input
        ip = "aish"
        expected = "Invalid input"
        result = prime_num(ip)
        self.assertEqual(expected, result)

    def test_prime_num_for_None(self):
        ip = None
        expected = None
        result = prime_num(ip)
        self.assertEqual(expected, result)