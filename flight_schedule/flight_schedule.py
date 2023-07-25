# flight_schedule.py
import json

def get_available_flights(source, destination, date):
    """
    Retrieves available flights for a given date and route from flights.json.

    Args:
        source (str): The source airport code.
        destination (str): The destination airport code.
        date (str): The date for which available flights are to be retrieved.

    Returns:
        list: A list of dictionaries containing the available flights for the given date and route.
    """
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

def update_flight_schedule(flight_id, new_schedule):
    """
    Updates the schedule of a flight and updates the flights.json file.

    Args:
        flight_id (str): The ID of the flight whose schedule is being updated.
        new_schedule (str): The updated schedule for the flight.
    """
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
