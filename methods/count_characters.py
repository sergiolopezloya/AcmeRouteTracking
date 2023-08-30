"""
count_characters module

This module provides functions to count vowels and consonants in a string.
"""
def count_vowels(string_counted):
    """
    Count the number of vowels in a string.

    Args:
        string_counted (str): The input string.

    Returns:
        int: The count of vowels in the string.
    """
    vowels = "AEIOUaeiou"
    return sum(1 for char in string_counted if char in vowels)

def count_consonants(string_counted):
    """
    Count the number of consonants in a string.

    Args:
        string_counted (str): The input string.

    Returns:
        int: The count of consonants in the string.
    """
    consonants = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
    return sum(1 for char in string_counted if char in consonants)
