import unittest
from mini_parking_system import *
class TestParkingSystemAdvanced(unittest.TestCase):

    def setUp(self):
        self.parking = [0] * 20

    def park_car(self):
        for index in range(20):
            if self.parking[index] == 0:
                self.parking[index] = 1
                return index
        return -1

    def remove_car(self, slot):
        if 0 <= slot < 20 and self.parking[slot] == 1:
            self.parking[slot] = 0
            return True
        return False

    
    def test_park_and_remove(self):
        slot = self.park_car()
        self.assertNotEqual(slot, -1)

        removed = self.remove_car(slot)
        self.assertTrue(removed)
        self.assertEqual(self.parking[slot], 0)

    
    def test_remove_empty_slot(self):
        result = self.remove_car(5)
        self.assertFalse(result)

    
    def test_parking_order(self):
        self.park_car()
        self.park_car()
        self.park_car()

        self.assertEqual(self.parking[0], 1)
        self.assertEqual(self.parking[1], 1)
        self.assertEqual(self.parking[2], 1)

    
    def test_invalid_slot(self):
        self.assertFalse(self.remove_car(-1))
        self.assertFalse(self.remove_car(25))

    
    def test_reuse_slot(self):
        
        for _ in range(20):
            self.park_car()

        
        self.remove_car(10)

        
        new_slot = self.park_car()

        self.assertEqual(new_slot, 10)

if __name__ == "__main__":
    unittest.main()
