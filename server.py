from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Helper functions to interact with JSON files

def load_data(file_name):
    with open(file_name, "r") as f:
        data = json.load(f)
    return data

def save_data(file_name, data):
    with open(file_name, "w") as f:
        json.dump(data, f, indent=4)

# Routes for web pages

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/passengers")
def passengers():
    passengers_data = load_data("passengers.json")
    return render_template("passengers.html", passengers=passengers_data["passengers"])

@app.route("/flights")
def flights():
    flights_data = load_data("flights.json")
    return render_template("flights.html", flights=flights_data["flights"])

@app.route("/bookings")
def bookings():
    bookings_data = load_data("bookings.json")
    return render_template("bookings.html", bookings=bookings_data["bookings"])

# Routes for API endpoints to interact with JSON files

@app.route("/api/get_passenger/<passenger_id>")
def get_passenger(passenger_id):
    passengers_data = load_data("passengers.json")
    for passenger in passengers_data["passengers"]:
        if passenger["passenger_id"] == passenger_id:
            return jsonify(passenger)
    return jsonify({"message": "Passenger not found"}), 404

@app.route("/api/add_passenger", methods=["POST"])
def add_passenger():
    new_passenger = request.get_json()
    passengers_data = load_data("passengers.json")
    passengers_data["passengers"].append(new_passenger)
    save_data("passengers.json", passengers_data)
    return jsonify({"message": "Passenger added successfully"}), 201

@app.route("/api/delete_passenger/<passenger_id>", methods=["DELETE"])
def delete_passenger(passenger_id):
    passengers_data = load_data("passengers.json")
    passengers_data["passengers"] = [passenger for passenger in passengers_data["passengers"] if passenger["passenger_id"] != passenger_id]
    save_data("passengers.json", passengers_data)
    return jsonify({"message": "Passenger deleted successfully"}), 200

@app.route("/api/get_flight/<flight_id>")
def get_flight(flight_id):
    flights_data = load_data("flights.json")
    for flight in flights_data["flights"]:
        if flight["flight_id"] == flight_id:
            return jsonify(flight)
    return jsonify({"message": "Flight not found"}), 404

@app.route("/api/add_flight", methods=["POST"])
def add_flight():
    new_flight = request.get_json()
    flights_data = load_data("flights.json")
    flights_data["flights"].append(new_flight)
    save_data("flights.json", flights_data)
    return jsonify({"message": "Flight added successfully"}), 201

@app.route("/api/delete_flight/<flight_id>", methods=["DELETE"])
def delete_flight(flight_id):
    flights_data = load_data("flights.json")
    flights_data["flights"] = [flight for flight in flights_data["flights"] if flight["flight_id"] != flight_id]
    save_data("flights.json", flights_data)
    return jsonify({"message": "Flight deleted successfully"}), 200

@app.route("/api/get_booking/<booking_id>")
def get_booking(booking_id):
    bookings_data = load_data("bookings.json")
    for booking in bookings_data["bookings"]:
        if booking["booking_id"] == booking_id:
            return jsonify(booking)
    return jsonify({"message": "Booking not found"}), 404

@app.route("/api/add_booking", methods=["POST"])
def add_booking():
    new_booking = request.get_json()
    bookings_data = load_data("bookings.json")
    bookings_data["bookings"].append(new_booking)
    save_data("bookings.json", bookings_data)
    return jsonify({"message": "Booking added successfully"}), 201

@app.route("/api/delete_booking/<booking_id>", methods=["DELETE"])
def delete_booking(booking_id):
    bookings_data = load_data("bookings.json")
    bookings_data["bookings"] = [booking for booking in bookings_data["bookings"] if booking["booking_id"] != booking_id]
    save_data("bookings.json", bookings_data)
    return jsonify({"message": "Booking deleted successfully"}), 200

if __name__ == "__main__":
    app.run(debug=True)
