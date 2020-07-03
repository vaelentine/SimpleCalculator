import unittest
from parameterized import parameterized
from Calculator import Calculator

class CalculatorTest(unittest.TestCase):
    @parameterized.expand([
        (0, 1, 1),
        (0.15, 3, 3.15),
        (-0.15, -3, -3.15),
        (-1, 1, 0),
        (-1.4, 0.5, -0.9),
        (-0.4, 0.5, 0.1)
    ])
    def test_add(self, addend_a, addend_b, result_sum):
        calculator = Calculator()
        self.assertEqual(calculator.add(addend_a, addend_b), result_sum)

    @parameterized.expand([
        (0, 1, -1),
        (0.15, 3, -2.85),
        (-0.15, 3, -3.15),
        (-1, 1, -2),
        (-1.4, 0.5, -1.9),
        (1.4, 0.5, 0.9)
    ])
    def test_subtract(self, minuend, subtrahend, difference):
        calculator = Calculator()
        self.assertEqual(calculator.subtract(minuend, subtrahend), difference)
    @parameterized.expand([
        (1, 1, 1),
        (2, 2, 4),
        (1, 2, 2),
        (4, 1, 4),
        (4, 4, 16),
        (3.3, 3, 9.9),
        (1.5, -2, -3)
    ])
    def test_multiply(self, multiplier, multiplicand, product):
        calculator = Calculator()
        self.assertEqual(calculator.multiply(multiplier, multiplicand), product)
if __name__ == "__main__":
    unittest.main()
