# loyalty_status.py
import csv

def calculate_loyalty_status(passenger_id):
    """
    Calculates the loyalty status of a passenger based on their booking history in bookings.csv.

    Args:
        passenger_id (str): The ID of the passenger whose loyalty status is to be calculated.

    Returns:
        str: The calculated loyalty status ('Gold' or 'Silver').
    """
    # Code to calculate passenger loyalty status based on bookings.csv
    with open("bookings.csv", "r") as f:
        reader = csv.DictReader(f)
        passenger_bookings = [booking for booking in reader if booking["passenger_id"] == passenger_id]

    total_bookings = len(passenger_bookings)
    return "Gold" if total_bookings >= 10 else "Silver"