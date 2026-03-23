import unittest
from moves_zero_end import move_zeros
class TestMoveZeros(unittest.TestCase):
    def test_mixed_numbers(self):
        array = [5,0,3,0,2,0]
        result = move_zeros(array)
        self.assertEqual(result,[5,3,2,0,0,0])


    def test_no_zeros(self):
        array = [1,2,3,]
        result = move_zeros(array)
        self.assertEqual(result,[1,2,3])
if __name__ == "__main__":
    unittest.main()
