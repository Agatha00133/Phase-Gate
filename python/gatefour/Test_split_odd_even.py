import unittest
from split_odd_even import split_even_odd
class TestSplitOddEven(unittest.TestCase):

    def test_mixed_numbers(self):
        array = [45,60,3,10,9,22]
        result = split_even_odd(array)
        self.assertEqual(result,[[45,3,9],[60,10,22]])

    def test_empty_array(self):
        array = []
        result = split_even_odd(array)
        self.assertEqual(result,[[],[]])
if __name__ == "__main__":
    unittest.main()
