import unittest
from Array_length import number_length
class Arraylength(unittest.TestCase):
    def test_that_input(self):
        self.asserEqual(number_length[10,11,12,-1,-1])

if __name__ == "__main__":
    unittest.main()
