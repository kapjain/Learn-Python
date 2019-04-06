import unittest
from unittestEx import calc
# import calc uncomment itwhen you want to execute testcase otherwise it will throw errro

class TestCalc(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(calc.add(2,3), 5)
        self.assertEqual(calc.add(-2,3), 1)
        self.assertEqual(calc.add(-2,-3), -5)
        self.assertEqual(calc.add(0,3), 3)
        
    def test_sub(self):
        self.assertEqual(calc.sub(2,3), -1)
        self.assertEqual(calc.sub(-2,3), -5)
        self.assertEqual(calc.sub(-2,-3), 1)
        self.assertEqual(calc.sub(0,3), -3)
    
    def test_mul(self):
        self.assertEqual(calc.mul(2,3), 6)
        self.assertEqual(calc.mul(-2,3), -6)
        self.assertEqual(calc.mul(-2,-3), 6)
        self.assertEqual(calc.mul(0,3), 0)
        
    def test_div(self):
        self.assertEqual(calc.div(3,3), 1)
        self.assertEqual(calc.div(-2,2), -1)
        self.assertEqual(calc.div(-6,-3), 2)
        self.assertEqual(calc.div(0,3), 0)
        
        self.assertRaises(ValueError, calc.div,10,0)
        
        with self.assertRaises(ValueError):
            calc.div(10,0)
            


if __name__ == '__main__':
    unittest.main()