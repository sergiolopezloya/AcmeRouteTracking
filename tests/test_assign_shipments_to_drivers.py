"""
Test Module for assign_shipments_to_drivers Method

This module contains test cases for the assign_shipments_to_drivers method
in the main program.
"""
import unittest
from main import assign_shipments_to_drivers

class TestAssignShipmentsToDriversModule(unittest.TestCase):
    """
    Test cases for the assign_shipments_to_drivers method.
    """
    def test_assign_shipments_to_drivers(self):
        """
        Test the assign_shipments_to_drivers function with different scenarios.

        Test case 1: Basic test with one driver and one destination.
        Test case 2: Multiple drivers and destinations with equal suitability score.
        """
        # Test case 1: Basic test with one driver and one destination
        destinations = ["Destination A"]
        drivers = ["Driver 1"]
        expected_result = (4, {"Destination A": "Driver 1"})
        self.assertEqual(assign_shipments_to_drivers(destinations, drivers), expected_result)

        # Test case 2: Multiple drivers and destinations with equal suitability score
        destinations = ["Destination A", "Destination B", "Destination C"]
        drivers = ["Driver 1", "Driver 2", "Driver 3"]
        expected_result = (12, {"Destination A": "Driver 1", "Destination B": "Driver 2", "Destination C": "Driver 3"})
        self.assertEqual(assign_shipments_to_drivers(destinations, drivers), expected_result)

if __name__ == '__main__':
    unittest.main()
