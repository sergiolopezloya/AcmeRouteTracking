import unittest
from unittest.mock import patch
from io import StringIO
from main import main

class TestMainModule(unittest.TestCase):

    @patch('builtins.input', side_effect=['n'])  # Simulate user input 'n'
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_without_explanation(self, mock_stdout, mock_input):
        main()
        output = mock_stdout.getvalue().strip()
        # Perform assertions on the output
        self.assertIn("Total Suitability Score:", output)
        self.assertIn("Matching:", output)
        self.assertNotIn("Explain:", output)  # Explain: should not be included

    @patch('builtins.input', side_effect=['y'])  # Simulate user input 'y'
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_with_explanation(self, mock_stdout, mock_input):
        main()
        output = mock_stdout.getvalue().strip()
        print(">>>", output)
        # Perform assertions on the output
        self.assertIn("Total Suitability Score:", output)
        self.assertIn("Matching:", output)
        self.assertIn("Explain:", output)  # Explain: should be included

if __name__ == '__main__':
    unittest.main()
