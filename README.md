The aviation domain-related project consists of three interconnected repositories: flight_booking, passenger_management, and flight_schedule; a flask server and a frontend user interface. Each repository contains a set of Python files, JSON, and CSV files to manage flight bookings, passenger information, and flight schedules.

The 'flight_booking" repository handles flight booking operations. It contains five files:

flight_booking.py: Defines functions to book flights, cancel bookings, and process payments. The book_flight() function enables users to book a flight with details like flight ID, passenger ID, and seat number. cancel_booking() cancels a booking by updating the booking status. make_payment() processes the payment for a booking.
bookings.json: Stores the flight booking details, including booking ID, flight ID, passenger ID, seat number, and status.
passenger_info.py: Retrieves passenger information using the get_passenger_info() function, which accesses data from the passengers.json file.
payment.py: Contains payment processing logic. It updates the booking status to "paid" in the bookings.json file once a successful payment is processed.
cancellation.py: Enables users to cancel a booking and updates the booking status to "cancelled" in the bookings.json file.

This "passenger_management" manages passenger-related information. It consists of five files:

passenger_management.py: Contains functions to add passengers and update their contact information. add_passenger() creates a new passenger entry with details like name, age, and contact information. update_contact_info() allows modifying the passenger's contact details.
passengers.json: Stores passenger data, including passenger ID, name, age, and contact information.
booking_history.py: Enables users to retrieve a passenger's booking history using the get_booking_history() function, which accesses data from the bookings.csv file.
loyalty_status.py: Calculates the passenger's loyalty status based on their number of bookings using the calculate_loyalty_status() function. The status is determined from the bookings.csv file.
update_contact.py: Similar to passenger_management.py, this file allows updating the passenger's contact information.

The "flight_schedule" repository deals with flight schedules and availability. It includes five files:

flight_schedule.py: Provides functionality to retrieve available flights, check flight status, and update flight schedules. get_available_flights() returns a list of available flights for a given route and date, using data from the flights.json file. get_flight_status() allows checking the status of a specific flight. update_flight_schedule() lets users modify the schedule of a flight.
flights.json: Contains flight schedule details, such as flight ID, source, destination, date, status, and schedule.
seat_map.py: Fetches the seat map for a particular flight using the get_seat_map() function, which retrieves data from the seats.csv file.
flight_status.py: Similar to flight_schedule.py, this file checks the status of a flight based on data from the flights.json file.
update_schedule.py: Enables users to update the schedule of a flight using the update_flight_schedule() function, modifying the data in the flights.json file.

The server is a Flask application that acts as the backend for our airline system. It provides API endpoints to handle flight booking, canceling bookings, and getting flight status. The server uses JSON files (bookings.json, passengers.json, and flights.json) and interactions with the corresponding repositories (flight_booking, passenger_management, and flight_schedule) to manage flight bookings and status.

The HTML file represents a frontend user interface for the flight booking application. It includes a form where users can enter their flight details (e.g., flight ID, passenger ID, seat number) and a button to book the flight. When the user submits the booking form or when the page loads, the JavaScript code interacts with the server to book a flight or retrieve the status of a specific flight.
