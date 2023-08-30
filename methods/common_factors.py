"""
common_factors module

This module provides a function to check for common factors between two numbers.
"""
def common_factors(dest_length, driver_length):
    """
    Check if there are common factors between two numbers.

    Args:
        dest_length (int): Length of the destination street name.
        driver_length (int): Length of the driver's name.

    Returns:
        bool: True if there are common factors, False otherwise.
    """
    for i in range(2, min(dest_length, driver_length) + 1):
        if dest_length % i == 0 and driver_length % i == 0:
            return True
    return False
