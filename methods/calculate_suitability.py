from methods.common_factors import common_factors
from methods.count_characters import count_consonants, count_vowels


def calculate_suitability(destination, driver):
    """
    Calculate the suitability score for assigning a driver to a shipment destination.

    Args:
        destination (str): The shipment's destination street name.
        driver (str): The driver's name.

    Returns:
        float: The suitability score for the assignment.
    """
    dest_length = len(destination)
    driver_length = len(driver)

    base_suitability_score = 0
    if dest_length % 2 == 0:
        base_suitability_score = count_vowels(driver) * 1.5
    else:
        base_suitability_score = count_consonants(driver)

    suitability_score = base_suitability_score
    if common_factors(dest_length, driver_length):
        suitability_score *= 1.5

    return suitability_score
