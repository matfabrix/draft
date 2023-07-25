# flight_schedule.py
import json

def get_available_flights(source, destination, date):
    # Code to retrieve available flights for a given date and route from flights.json
    with open("flights.json", "r") as f:
        flights_data = json.load(f)

    available_flights = [
        flight for flight in flights_data["flights"]
        if flight["source"] == source
        and flight["destination"] == destination
        and flight["date"] == date
    ]

    return available_flights

def get_flight_status(flight_id):
    # Code to check the status of a flight from flights.json
    with open("flights.json", "r") as f:
        flights_data = json.load(f)

    for flight in flights_data["flights"]:
        if flight["flight_id"] == flight_id:
            return flight["status"]

    return None

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
