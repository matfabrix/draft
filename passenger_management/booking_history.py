# booking_history.py
import csv

def get_booking_history(passenger_id):
    """
    Retrieves the booking history of a passenger from bookings.csv.

    Args:
        passenger_id (str): The ID of the passenger whose booking history is to be retrieved.

    Returns:
        list: A list of dictionaries containing the booking history, or an empty list if not found.
    """
    # Code to retrieve booking history from bookings.csv
    with open("bookings.csv", "r") as f:
        reader = csv.DictReader(f)
        booking_history = [booking for booking in reader if booking["passenger_id"] == passenger_id]

    return booking_history
