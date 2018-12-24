from unittest import  TestCase
from amstrong_number import  amstrong_num


class TestAmstrongNumber(TestCase):

    def test_amstrong_num_for_sucess(self):
        ip = 153
        expected = True
        result = amstrong_num(ip)
        self.assertEqual(expected, result)

    def test_amstrong_num_for_failure(self):
        ip = 752
        expected = False
        result = amstrong_num(ip)
        self.assertEqual(expected, result)

    def test_amstrong_num_for_empty_string_or_string(self):
        #empty string input
        ip = ""
        expected = "Invalid input"
        result = amstrong_num(ip)
        self.assertEqual(expected, result)

        #string input
        ip = "aish"
        expected = "Invalid input"
        result = amstrong_num(ip)
        self.assertEqual(expected, result)

    def test_amstrong_num_for_None(self):
        ip = None
        expected = None
        result = amstrong_num(ip)
        self.assertEqual(expected, result)