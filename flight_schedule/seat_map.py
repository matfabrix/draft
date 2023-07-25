# seat_map.py
import csv

def get_seat_map(flight_id):
    """
    Retrieves the seat map for a given flight from seats.csv.

    Args:
        flight_id (str): The ID of the flight whose seat map is to be retrieved.

    Returns:
        list: A list of dictionaries containing the seat map, or an empty list if not found.
    """
    # Code to retrieve seat map for a given flight from seats.csv
    with open("seats.csv", "r") as f:
        reader = csv.DictReader(f)
        seat_map = [seat for seat in reader if seat["flight_id"] == flight_id]

    return seat_map