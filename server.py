from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Load initial data from JSON files
with open("flight_booking/bookings.json", "r") as f:
    bookings_data = json.load(f)

with open("passenger_management/passengers.json", "r") as f:
    passengers_data = json.load(f)

with open("flight_schedule/flights.json", "r") as f:
    flights_data = json.load(f)

# Booking a flight
@app.route("/book_flight", methods=["POST"])
def book_flight():
    data = request.get_json()
    flight_id = data.get("flight_id")
    passenger_id = data.get("passenger_id")
    seat_number = data.get("seat_number")

    # Perform booking operations here using the functions from flight_booking.py
    # E.g., flight_booking.book_flight(flight_id, passenger_id, seat_number)

    return jsonify({"message": "Flight booked successfully!"})

# Canceling a booking
@app.route("/cancel_booking", methods=["POST"])
def cancel_booking():
    data = request.get_json()
    booking_id = data.get("booking_id")

    # Perform cancellation operations here using the functions from flight_booking.py
    # E.g., flight_booking.cancel_booking(booking_id)

    return jsonify({"message": "Booking cancelled successfully!"})

# Getting flight status
@app.route("/flight_status/<flight_id>", methods=["GET"])
def get_flight_status(flight_id):
    # Perform status retrieval here using the functions from flight_schedule.py
    # E.g., flight_schedule.get_flight_status(flight_id)

    # For demonstration purposes, we'll return a dummy response
    return jsonify({"flight_id": flight_id, "status": "on time"})

if __name__ == "__main__":
    app.run(debug=True)