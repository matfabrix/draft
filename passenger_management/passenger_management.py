# passenger_management.py
import json

def add_passenger(name, age, contact_info):
    # Code to add a new passenger and update passengers.json
    with open("passengers.json", "r") as f:
        passengers_data = json.load(f)

    passenger_id = f"PS{len(passengers_data['passengers']) + 1}"

    passenger = {
        "passenger_id": passenger_id,
        "name": name,
        "age": age,
        "contact_info": contact_info
    }

    passengers_data["passengers"].append(passenger)

    with open("passengers.json", "w") as f:
        json.dump(passengers_data, f, indent=4)

def update_contact_info(passenger_id, new_contact_info):
    # Code to update passenger contact information and update passengers.json
    with open("passengers.json", "r") as f:
        passengers_data = json.load(f)

    for passenger in passengers_data["passengers"]:
        if passenger["passenger_id"] == passenger_id:
            passenger["contact_info"] = new_contact_info
            break

    with open("passengers.json", "w") as f:
        json.dump(passengers_data, f, indent=4)

# Additional functions as needed
