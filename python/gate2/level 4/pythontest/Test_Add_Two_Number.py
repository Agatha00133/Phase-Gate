import unittest
from Add_Two_Number import adds_number 

class TestAddTwoNumber(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(adds_number(2, 3), 5)

    def test_negative_numbers(self):
        self.assertEqual(adds_number(-1, -1), -2)

    def test_mixed_numbers(self):
        self.assertEqual(adds_number(-1, 1), 0)

if __name__ == "__main__":
    unittest.main()
