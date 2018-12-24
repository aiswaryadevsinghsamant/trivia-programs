from unittest import TestCase
from swap_two_numbers import swap_using_thirdvariable, swap_without_thirdvariable


class TestSwapTwoNumbers(TestCase):

    def test_swap_using_thirdvariable_for_success(self):
        ip_a = 5
        ip_b = 4
        expected = 4, 5
        result = swap_using_thirdvariable(ip_a, ip_b)
        self.assertEqual(expected, result)

    def test_swap_using_thirdvariable_for_empty_string_or_string(self):
        # empyt strin input
        ip_a = ""
        ip_b = ""
        expected = "Invalid input"
        result = swap_using_thirdvariable(ip_a, ip_b)
        self.assertEqual(expected, result)


        # String input
        ip_a = "aish"
        ip_b = "abhi"
        expected = "Invalid input"
        result = swap_using_thirdvariable(ip_a, ip_b)
        self.assertEqual(expected, result)

    def test_swap_using_thirdvariable_for_None(self):
        ip_a = None
        ip_b = None
        expected = None
        result = swap_using_thirdvariable(ip_a, ip_b)
        self.assertEqual(expected, result)




    def test_swap_without_thirdvariable_for_success(self):
        ip_a = 7
        ip_b = 5
        expected = 5, 7
        result = swap_without_thirdvariable(ip_a, ip_b)
        self.assertEqual(expected, result)

    def test_swap_without_thirdvariable_for_empty_string_or_string(self):
        #empty string input
        ip_a = ""
        ip_b = ""
        expected = "Invalid input"
        result = swap_without_thirdvariable(ip_a, ip_b)
        self.assertEqual(expected, result)

        ##string input
        ip_a = "aish"
        ip_a = "abhi"
        expected = "Invalid input"
        result = swap_without_thirdvariable(ip_a, ip_b)
        self.assertEqual(expected, result)