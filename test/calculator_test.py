import unittest
from parameterized import parameterized
from Calculator import Calculator

class CalculatorTest(unittest.TestCase):
    calculator = Calculator()
    
    @parameterized.expand([
        (0, 1, 1),
        (0.15, 3, 3.15),
        (-0.15, -3, -3.15),
        (-1, 1, 0),
        (-1.4, 0.5, -0.9),
        (-0.4, 0.5, 0.1),
    ])
    def test_add(self, addend_a, addend_b, result_sum):
        self.assertEqual(self.calculator.add(addend_a, addend_b), result_sum)

    @parameterized.expand([
        (0, 1, -1),
        (0.15, 3, -2.85),
        (-0.15, 3, -3.15),
        (-1, 1, -2),
        (-1.4, 0.5, -1.9),
        (1.4, 0.5, 0.9),
    ])
    def test_subtract(self, minuend, subtrahend, difference):
        self.assertEqual(self.calculator.subtract(minuend, subtrahend), difference)
    
    @parameterized.expand([
        (1, 1, 1),
        (2, 2, 4),
        (1, 2, 2),
        (4, 1, 4),
        (4, 4, 16),
        (3.3, 3, 9.9),
        (1.5, -2, -3),
    ])
    def test_multiply(self, multiplier, multiplicand, product):
        self.assertEqual(self.calculator.multiply(multiplier, multiplicand), product)

    @parameterized.expand([
        (1, 1, 1),
        (2, 1, 2),
        (4, 2, 2),
        (6, 2, 3),
        (3, 2, 1.5),
        (-4, 2, -2),
        (0, 1, 0),
        (9, -2, -4.5),
        ])   
    def test_divide(self, dividend, divisor, quotient):
        self.assertEqual(self.calculator.divide(dividend, divisor), quotient)

if __name__ == "__main__":
    unittest.main()
