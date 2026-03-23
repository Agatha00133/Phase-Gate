import unittest
from dulicate_element import find_duplicates
class TestFindDuplicates(unittest.TestCase):

    def test_with_duplicates(self):
        array = [45,60,3,0,67,2,45,3,22,0]
        result = find_duplicates(array)
        self.assertCountEqual(result,[45,3,0])

    def test_no_duplicates(self):
       array = [1,2,3,4]
       result = find_duplicates(array)
       self.assertEqual(result,[])

if __name__ == "__main__":
    unittest.main()
