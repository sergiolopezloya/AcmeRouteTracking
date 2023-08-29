def calculate_suitability(destination, driver):
    """
    Calculate the suitability score for assigning a driver to a shipment destination.

    Args:
        destination (str): The shipment's destination street name.
        driver (str): The driver's name.

    Returns:
        float: The suitability score for the assignment.
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

    dest_length = len(destination)
    driver_length = len(driver)

    base_suitability_score = 0
    if dest_length % 2 == 0:
        base_suitability_score = count_vowels(driver) * 1.5
    else:
        base_suitability_score = count_consonants(driver)

    common_factors = set()
    for i in range(2, min(dest_length, driver_length) + 1):
        if dest_length % i == 0 and driver_length % i == 0:
            common_factors.add(i)

    suitability_score = base_suitability_score
    if common_factors:
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
    # Read input files, call functions, and print results
    with open('destinations.txt', 'r', encoding='utf-8') as dest_file, \
          open('drivers.txt', 'r', encoding='utf-8') as driver_file:
        destinations = dest_file.read().splitlines()
        drivers = driver_file.read().splitlines()

    total_ss, matching = assign_shipments_to_drivers(destinations, drivers)

    print("Total Suitability Score:", total_ss)
    print("Matching:")
    for destination, driver in matching.items():
        print(f"{destination} -> {driver}")

if __name__ == "__main__":
    main()
