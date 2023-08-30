# Acme Route Tracking

Acme Route Tracking is a Python program that assigns shipment destinations to drivers based on suitability scores. The program reads shipment destinations and driver names from input files, calculates suitability scores, and then matches shipments with drivers to maximize the total suitability score.

## Methods

The program consists of several methods that contribute to the assignment process:

- `calculate_suitability(destination, driver)`: Calculates the suitability score for assigning a driver to a shipment destination.
- `common_factors(dest_length, driver_length)`: Checks if there are common factors between two numbers.
- `count_consonants(string_counted)`: Counts the number of consonants in a string.
- `count_vowels(string_counted)`: Counts the number of vowels in a string.
- `assign_shipments_to_drivers(destinations, drivers)`: Assigns shipment destinations to drivers to maximize the total suitability score.

## Instructions

1. Clone this repository or download the source code.
2. Make sure you have Python 3 installed on your system.
3. Run the program by executing the `main.py` file:

````
python3 main.py
````

4. Follow the prompts to provide input for shipment destinations and driver names.
5. The program will display the total suitability score and the matching of shipments to drivers.

## Project Structure

```
_AcmeRouteTracking/_
├── _methods/_
│ ├── __init__.py
│ ├── assign_shipments_to_drivers.py
│ ├── calculate_suitability.py
│ ├── common_factors.py
│ ├── count_characters.py
├── _tests/_
│ ├── __init__.py
│ ├── test_assign_shipments_to_drivers.py
│ ├── test_calculate_suitability.py
│ ├── test_common_factors.py
│ ├── test_count_characters.py
├── main.py
├── destinations.txt
├── drivers.txt
├── LICENSE
├── README.md
```

## Running Tests

To run the tests, use the following command in your terminal from the root directory of the project:

```
python3 -m unittest discover tests
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- **[Sergio Lopez](https://github.com/sergiolopezloya)** - _Personal project_