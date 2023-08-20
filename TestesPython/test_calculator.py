import unittest
from calculadora import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
    
    def test_add(self):
        self.assertEqual(self.calculator.add(2,3),5)
        self.assertEqual(self.calculator.add(1,3),)
        self.assertEqual(self.calculator.add(2,2),4)
    
    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(3,3),0)
        self.assertEqual(self.calculator.subtract(6,3),3)
        self.assertEqual(self.calculator.subtract(8,2),6)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(2,6),12)
        self.assertEqual(self.calculator.multiply(3,6),18)
        self.assertEqual(self.calculator.multiply(1,6),6)

    def teste_divide(self):
        self.assertEqual(self.calculator.divide(4,2),2)
        self.assertEqual(self.calculator.divide(3,3),1)

if __name__ == '__main__':
    unittest.main()
