# passenger_info.py
import json

def get_passenger_info(passenger_id):
    """
    Retrieves passenger information from passengers.json based on the given passenger ID.

    Args:
        passenger_id (str): The ID of the passenger whose information is to be retrieved.

    Returns:
        dict: The passenger information as a dictionary, or None if not found.
    """
    # Code to retrieve passenger information from passengers.json
    with open("passengers.json", "r") as f:
        passengers_data = json.load(f)

    for passenger in passengers_data["passengers"]:
        if passenger["passenger_id"] == passenger_id:
            return passenger

    return None
