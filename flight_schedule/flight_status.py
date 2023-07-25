# flight_status.py
import json

def get_flight_status(flight_id):
    # Code to check the status of a flight from flights.json
    with open("flights.json", "r") as f:
        flights_data = json.load(f)

    for flight in flights_data["flights"]:
        if flight["flight_id"] == flight_id:
            return flight["status"]

    return None

# Additional functions as needed
