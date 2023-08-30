import unittest
from methods.count_characters import count_consonants, count_vowels

class TestCountCharacters(unittest.TestCase):
    """
    Test cases for the count_vowels and count_consonants functions.
    """

    def test_count_vowels(self):
        """
        Test vowel counting.
        """
        self.assertEqual(count_vowels("John"), 1)
        self.assertEqual(count_vowels("Alice"), 3)

    def test_count_consonants(self):
        """
        Test consonant counting.
        """
        self.assertEqual(count_consonants("John"), 3)
        self.assertEqual(count_consonants("Alice"), 2)

if __name__ == '__main__':
    unittest.main()
