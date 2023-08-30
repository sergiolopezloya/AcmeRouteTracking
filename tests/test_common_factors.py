import unittest
from methods.common_factors import common_factors

class TestCommonFactors(unittest.TestCase):
    """
    Test cases for the common_factors function.
    """

    def test_common_factors(self):
        """
        Test common factors calculation.
        """
        self.assertTrue(common_factors(4, 6))
        self.assertFalse(common_factors(5, 9))
        self.assertTrue(common_factors(10, 20))

if __name__ == '__main__':
    unittest.main()
