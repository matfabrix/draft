from flask import Flask, request, jsonify

app = Flask(__name__)

# Initialize data
flights_data = []
bookings_data = []
passengers_data = []

# Function to find a flight by ID
def find_flight(flight_id):
    for flight in flights_data:
        if flight["flight_id"] == flight_id:
            return flight
    return None

# Function to find a booking by ID
def find_booking(booking_id):
    for booking in bookings_data:
        if booking["booking_id"] == booking_id:
            return booking
    return None

# Function to find a passenger by ID
def find_passenger(passenger_id):
    for passenger in passengers_data:
        if passenger["passenger_id"] == passenger_id:
            return passenger
    return None

# Add a new flight
@app.route("/add_flight", methods=["POST"])
def add_flight():
    flight_data = request.get_json()
    flights_data.append(flight_data)
    return jsonify({"message": "Flight added successfully!"})

# Book a flight
@app.route("/book_flight", methods=["POST"])
def book_flight():
    booking_data = request.get_json()
    flight_id = booking_data["flight_id_book"]
    passenger_id = booking_data["passenger_id"]

    flight = find_flight(flight_id)
    if not flight:
        return jsonify({"message": f"Flight with ID {flight_id} not found."}), 404

    passenger = find_passenger(passenger_id)
    if not passenger:
        return jsonify({"message": f"Passenger with ID {passenger_id} not found."}), 404

    if "bookings" not in flight:
        flight["bookings"] = []

    seat_number = booking_data["seat_number"]
    booking_id = len(flight["bookings"]) + 1

    booking = {
        "booking_id": booking_id,
        "flight_id": flight_id,
        "passenger_id": passenger_id,
        "seat_number": seat_number
    }

    flight["bookings"].append(booking)
    bookings_data.append(booking)

    return jsonify({"message": "Flight booked successfully!"})

# Cancel a booking
@app.route("/cancel_booking", methods=["POST"])
def cancel_booking():
    booking_data = request.get_json()
    booking_id = booking_data["booking_id"]

    booking = find_booking(booking_id)
    if not booking:
        return jsonify({"message": f"Booking with ID {booking_id} not found."}), 404

    flight_id = booking["flight_id"]
    flight = find_flight(flight_id)
    if not flight:
        return jsonify({"message": f"Flight with ID {flight_id} not found."}), 404

    flight["bookings"].remove(booking)
    bookings_data.remove(booking)

    return jsonify({"message": "Booking canceled successfully!"})

# Get flight schedule
@app.route("/flight_schedule", methods=["GET"])
def get_flight_schedule():
    return jsonify({"flights": flights_data})

# Get bookings
@app.route("/bookings", methods=["GET"])
def get_bookings():
    return jsonify({"bookings": bookings_data})

# Get passengers
@app.route("/passengers", methods=["GET"])
def get_passengers():
    return jsonify({"passengers": passengers_data})

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/", methods=["GET"])
def show_html():
    return send_file("index.html")

if __name__ == "__main__":
    app.run(debug=True)