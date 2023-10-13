import unittest
from Calculation import Calculations

class TestCalculations(unittest.TestCase):
    def setUp(self):
        """
        Set up an instance of the Calculations class for testing.
        """
        self.math = Calculations()

    def test_add(self):
        """
        Test the 'add' method of the Calculations class.
        It checks if the addition operation produces the correct result.
        """
        result = self.math.add(2, 3)
        self.assertEqual(result, 5)

    def test_subtract(self):
        """
        Test the 'subtract' method of the Calculations class.
        It checks if the subtraction operation produces the correct result.
        """
        result = self.math.subtract(5, 2)
        self.assertEqual(result, 3)

    def test_wrong_add(self):
        """
        Test the 'add' method with incorrect input.
        It checks if the result is not equal to the incorrect expected result.
        """
        result = self.math.add(7, 2)
        self.assertNotEqual(result, 10)

    def test_random_subtract(self):
        """
        Test a random subtraction operation with the 'subtract' method.
        It checks if the result is not equal to a random expected value.
        """
        result = self.math.subtract(10, 4)
        self.assertNotEqual(result, 5) 

if __name__ == '__main__':
    unittest.main()
