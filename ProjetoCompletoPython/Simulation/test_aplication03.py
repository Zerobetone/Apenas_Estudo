import unittest
from aplication03 import Calculator


class TestCalculator(unittest.TestCase):
    
    def setUp(self):
        self.calc = Calculator()

    
    def testadd(self):
        self.assertEqual(self.calc.add(4,5), 9)

    def testsubtract(self):
        self.assertEqual(self.calc.subtract(8,2),6)

if __name__ == "__main__":
    unittest.main()