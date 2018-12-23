import unittest
from reverse_of_numbers import reverse


class TestReverseOfNumbers(unittest.TestCase):

    def test_reverse_for_success(self):
        ip = 21
        expected = 12
        result = reverse(ip)
        self.assertEqual(expected, result)

    def test_reverse_for_failure(self):
        ip = 35
        expected = 35
        result = reverse(ip)
        self.assertNotEqual(expected, result)

    def test_reverse_for_None(self):
        ip = None
        expected = None
        result = reverse(ip)
        self.assertEqual(expected, result)

    def test_reverse_for_empty_string(self):
        ip = ""
        expected = ""
        result = reverse(ip)
        self.assertEqual(expected, result)

    def test_reverse_for_string(self):
        ip = "abc"
        expected = "invalid input"
        result = reverse(ip)
        self.assertEqual(expected, result)

    def test_reverse_for_negative_numbers(self):
        ip = -12
        expected = "invalid input"
        result = reverse(ip)
        self.assertEqual(expected, result)
