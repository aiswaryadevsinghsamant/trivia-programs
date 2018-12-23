import unittest
from palindrome import palindrome_fun


class TestPalindrome(unittest.TestCase):

    def test_palindrome_fun_for_success(self):
        ip = 121
        expected = True
        result = palindrome_fun(ip)
        self.assertEqual(expected, result)

    def test_palindrome_fun_for_failure(self):
        ip = 153
        expected = False
        result = palindrome_fun(ip)
        self.assertEqual(expected, result)

    def test_palindrome_fun_for_empty_string_or_string(self):
        ip = ""
        expected = "invalid input"
        result = palindrome_fun(ip)
        self.assertEqual(expected, result)

        #String input
        ip = "pinks"
        expected = "invalid input"
        result = palindrome_fun(ip)
        self.assertEqual(expected, result)

    def test_palindrome_fun_for_negative_numbers(self):
        ip = -242
        expected = False
        result = palindrome_fun(ip)
        self.assertEqual(expected, result)

