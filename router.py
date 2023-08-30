from methods.assign_shipments_to_drivers import assign_shipments_to_drivers
from methods.calculate_suitability import calculate_suitability
from methods.common_factors import common_factors
from methods.count_characters import count_consonants, count_vowels


suitability_score = 0

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

    include_explanation = input("Do you want to include explanations? (Y/n): ").lower() or 'y'

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

            if include_explanation == 'y':
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
                explanation = f"({explanation})"

            print(f"{index}. {destination} -> {assigned_driver} {explanation}")

if __name__ == "__main__":
    main()
