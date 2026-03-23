import unittest
from Cheacks_Number import is_even 

class TestIsEven(unittest.TestCase):
    
    def test_even_number(self):
        self.assertTrue(is_even(4))  
    
    def test_odd_number(self):
        self.assertFalse(is_even(5))  
    
    def test_zero(self):
        self.assertTrue(is_even(0))  
    
    def test_negative_even(self):
        self.assertTrue(is_even(-2))  
    
    def test_negative_odd(self):
        self.assertFalse(is_even(-3))  

if __name__ == "__main__":
    unittest.main()
