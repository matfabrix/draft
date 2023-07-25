# payment.py
import json

def process_payment(booking_id, amount):
    # Code to process payment and update bookings.json
    with open("bookings.json", "r") as f:
        bookings_data = json.load(f)

    for booking in bookings_data["bookings"]:
        if booking["booking_id"] == booking_id:
            booking["status"] = "paid"
            break

    with open("bookings.json", "w") as f:
        json.dump(bookings_data, f, indent=4)

# Additional functions as needed
