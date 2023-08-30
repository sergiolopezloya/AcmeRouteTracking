import unittest
from methods.calculate_suitability import calculate_suitability, common_factors

class TestCalculateSuitability(unittest.TestCase):
    """
    Test cases for the calculate_suitability function.
    """

    def test_even_length_destination(self):
        """
        Test suitability calculation for an even length destination.
        """
        self.assertAlmostEqual(calculate_suitability("StreetA", "John"), 3)

    def test_odd_length_destination(self):
        """
        Test suitability calculation for an odd length destination.
        """
        self.assertAlmostEqual(calculate_suitability("StreetA2", "Alice"), 4.5)

    def test_common_factors(self):
        """
        Test common factors calculation.
        """
        self.assertTrue(common_factors(6, 9))
        self.assertFalse(common_factors(5, 9))

if __name__ == '__main__':
    unittest.main()
