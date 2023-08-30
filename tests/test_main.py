"""
Main Module Unit Tests

This module contains unit tests for the main function of the shipment assignment program.
It tests both scenarios: with and without including explanations in the output.

Test classes:
    TestMainModule: Contains test methods for the main function.

"""
import unittest
from unittest.mock import patch
from io import StringIO
from main import main

class TestMainModule(unittest.TestCase):
    """
    TestMainModule Class

    This class contains unit tests for the main function of the shipment assignment program.
    It tests both scenarios: with and without including explanations in the output.

    Test methods:
        test_main_without_explanation: Tests main's output without explanations.
        test_main_with_explanation: Tests the main function's output when explanations are included.

    """
    @patch('builtins.input', side_effect=['n'])  # Simulate user input 'n'
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_without_explanation(self, mock_stdout, mock_input):
        """
        Test the main function's output when explanations are not included.

        Simulates user input 'n' for not including explanations.
        Captures the standard output and performs assertions on the output.

        """
        main()
        output = mock_stdout.getvalue().strip()
        # Perform assertions on the output
        self.assertIn("Total Suitability Score:", output)
        self.assertIn("Matching:", output)
        self.assertNotIn("Explain:", output)  # Explain: should not be included

    @patch('builtins.input', side_effect=['y'])  # Simulate user input 'y'
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_with_explanation(self, mock_stdout, mock_input):
        """
        Test the main function's output when explanations are included.

        Simulates user input 'y' for including explanations.
        Captures the standard output and performs assertions on the output.

        """
        main()
        output = mock_stdout.getvalue().strip()
        print(">>>", output)
        # Perform assertions on the output
        self.assertIn("Total Suitability Score:", output)
        self.assertIn("Matching:", output)
        self.assertIn("Explain:", output)  # Explain: should be included

if __name__ == '__main__':
    unittest.main()
