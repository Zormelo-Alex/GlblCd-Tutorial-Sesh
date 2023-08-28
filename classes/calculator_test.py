from unittest import TestCase
from calc.calculator import Calculator

class CalculatorTest(TestCase):
    def test(self):
        self.assertTrue(True)

    def test_failing(self):
        self.assertTrue(False)

    def test_calculator_values_int(self):
        calculatorr = Calculator(24, 5 )