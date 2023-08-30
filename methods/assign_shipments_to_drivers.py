"""
assign_shipments_to_drivers module

This module provides a function to assign shipment destinations to drivers based
on suitability scores.
"""
from methods.calculate_suitability import calculate_suitability


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
            driver_suitability_score = calculate_suitability(
                destination, driver)
            if driver_suitability_score > max_ss and driver not in matching.values():
                max_ss = driver_suitability_score
                assigned_driver = driver

        if assigned_driver:
            matching[destination] = assigned_driver
            total_ss += max_ss

    return total_ss, matching
