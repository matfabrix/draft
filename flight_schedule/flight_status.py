# flight_status.py
import json

def get_flight_status(flight_id):
    """
    Retrieves the status of a flight from flights.json.

    Args:
        flight_id (str): The ID of the flight whose status is to be retrieved.

    Returns:
        str: The status of the flight, or None if not found.
    """
    # Code to check the status of a flight from flights.json
    with open("flights.json", "r") as f:
        flights_data = json.load(f)

    for flight in flights_data["flights"]:
        if flight["flight_id"] == flight_id:
            return flight["status"]

    return None