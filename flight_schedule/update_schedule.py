# update_schedule.py
import json

def update_flight_schedule(flight_id, new_schedule):
    # Code to update the flight schedule and update flights.json
    with open("flights.json", "r") as f:
        flights_data = json.load(f)

    for flight in flights_data["flights"]:
        if flight["flight_id"] == flight_id:
            flight["schedule"] = new_schedule
            break

    with open("flights.json", "w") as f:
        json.dump(flights_data, f, indent=4)

# Additional functions as needed
