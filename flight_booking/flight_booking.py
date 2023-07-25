# flight_booking.py
import json

def book_flight(flight_id, passenger_id, seat_number):
    # Code to book a flight and update bookings.json
    with open("bookings.json", "r") as f:
        bookings_data = json.load(f)

    booking = {
        "booking_id": f"BK{len(bookings_data['bookings']) + 1}",
        "flight_id": flight_id,
        "passenger_id": passenger_id,
        "seat_number": seat_number,
        "status": "confirmed"
    }

    bookings_data["bookings"].append(booking)

    with open("bookings.json", "w") as f:
        json.dump(bookings_data, f, indent=4)

def cancel_booking(booking_id):
    # Code to cancel a booking and update bookings.json
    with open("bookings.json", "r") as f:
        bookings_data = json.load(f)

    for booking in bookings_data["bookings"]:
        if booking["booking_id"] == booking_id:
            booking["status"] = "cancelled"
            break

    with open("bookings.json", "w") as f:
        json.dump(bookings_data, f, indent=4)

def make_payment(booking_id, amount):
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
