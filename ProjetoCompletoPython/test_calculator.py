import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
        self.calc.add_data(8)
        self.calc.add_data(6)
        self.calc.add_data(7)
        return self.calc
    
    def test_soma(self):
        self.assertEqual(self.calc.soma(), 21)
    
    def test_media(self):
        self.assertEqual(self.calc.mean(),7)

    def test_maior(self):
        self.assertEqual(self.calc.maior(), 8)

    def test_menor(self):
        self.assertEqual(self.calc.menor(), 6)

if __name__ == '__main__':
    unittest.main()