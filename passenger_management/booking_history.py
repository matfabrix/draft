# booking_history.py
import csv

def get_booking_history(passenger_id):
    # Code to retrieve booking history from bookings.csv
    with open("bookings.csv", "r") as f:
        reader = csv.DictReader(f)
        booking_history = [booking for booking in reader if booking["passenger_id"] == passenger_id]

    return booking_history

# Additional functions as needed
