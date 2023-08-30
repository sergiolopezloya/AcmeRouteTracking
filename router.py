suitability_score = 0
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

def assign_shipments_to_drivers(destinations, drivers):
    """
    Assign shipment destinations to drivers to maximize total suitability score.

    Args:
        destinations (list): List of shipment destination street names.
        drivers (list): List of driver names.

    Returns:
        tuple: A tuple containing the total suitability score and a dictionary
               matching shipment destinations to drivers.
    """
    total_ss = 0
    matching = {}

    for destination in destinations:
        max_ss = 0
        assigned_driver = None

        for driver in drivers:
            ss = calculate_suitability(destination, driver)
            if ss > max_ss and driver not in matching.values():
                max_ss = ss
                assigned_driver = driver

        if assigned_driver:
            matching[destination] = assigned_driver
            total_ss += max_ss

    return total_ss, matching

def main():
    """
    Main function to run the shipment assignment program.

    Reads shipment destinations and driver names from input files,
    assigns shipments to drivers based on suitability scores,
    and prints the results.

    """
    with open('destinations.txt', 'r', encoding='utf-8') as dest_file, \
          open('drivers.txt', 'r', encoding='utf-8') as driver_file:
        destinations = dest_file.read().splitlines()
        drivers = driver_file.read().splitlines()

    total_ss, matching = assign_shipments_to_drivers(destinations, drivers)

    print("Total Suitability Score:", total_ss)
    print("Matching:")
    assigned_drivers = set()  # To keep track of assigned drivers

    for index, destination in enumerate(destinations, start=1):
        max_ss = 0
        assigned_driver = None

        for driver in drivers:
            if driver in assigned_drivers:
                continue  # Skip already assigned drivers

            driver_suitability_score = calculate_suitability(destination, driver)
            if driver_suitability_score > max_ss:
                max_ss = driver_suitability_score
                assigned_driver = driver

        if assigned_driver:
            matching[destination] = assigned_driver
            assigned_drivers.add(assigned_driver)
            explanation = ""

            if len(destination) % 2 == 0:
                explanation = (
                    f"Vowel-based suitability (even length): "
                    f"{count_vowels(assigned_driver)} vowels * 1.5"
                )
            else:
                explanation = (
                    f"Consonant-based suitability (odd length): "
                    f"{count_consonants(assigned_driver)} consonants"
                )

            if common_factors(len(destination), len(assigned_driver)):
                explanation += " with common factors bonus (1.5x)"

            print(f"{index}. {destination} -> {assigned_driver} ({explanation})")

if __name__ == "__main__":
    main()
