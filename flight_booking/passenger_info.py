# passenger_info.py
import json

def get_passenger_info(passenger_id):
    # Code to retrieve passenger information from passengers.json
    with open("passengers.json", "r") as f:
        passengers_data = json.load(f)

    for passenger in passengers_data["passengers"]:
        if passenger["passenger_id"] == passenger_id:
            return passenger

    return None

# Additional functions as needed
