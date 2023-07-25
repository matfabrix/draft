# payment.py
import json

def process_payment(booking_id, amount):
    """
    Processes the payment for a flight booking and updates the bookings.json file.

    Args:
        booking_id (str): The ID of the booking for which payment is being processed.
        amount (float): The payment amount.
    """
    # Code to process payment and update bookings.json
    with open("bookings.json", "r") as f:
        bookings_data = json.load(f)

    for booking in bookings_data["bookings"]:
        if booking["booking_id"] == booking_id:
            booking["status"] = "paid"
            break

    with open("bookings.json", "w") as f:
        json.dump(bookings_data, f, indent=4)