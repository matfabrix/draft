# update_contact.py
import json

def update_contact_info(passenger_id, new_contact_info):
    """
    Updates the contact information of a passenger and updates the passengers.json file.

    Args:
        passenger_id (str): The ID of the passenger whose contact information is being updated.
        new_contact_info (str): The updated contact information.
    """
    # Code to update passenger contact information and update passengers.json
    with open("passengers.json", "r") as f:
        passengers_data = json.load(f)

    for passenger in passengers_data["passengers"]:
        if passenger["passenger_id"] == passenger_id:
            passenger["contact_info"] = new_contact_info
            break

    with open("passengers.json", "w") as f:
        json.dump(passengers_data, f, indent=4)