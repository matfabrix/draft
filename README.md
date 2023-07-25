ENGLISH:

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


ITALIANO:

Il progetto correlato al settore dell'aviazione è composto da tre repository interconnessi: flight_booking, passenger_management e flight_schedule; un server Flask e un'interfaccia utente frontend. Ogni repository contiene un insieme di file Python, JSON e CSV per gestire le prenotazioni dei voli, le informazioni sui passeggeri e gli orari dei voli.

Il repository "flight_booking" gestisce le operazioni di prenotazione dei voli. Contiene cinque file:

flight_booking.py: Definisce le funzioni per prenotare voli, annullare prenotazioni e processare i pagamenti. La funzione book_flight() consente agli utenti di prenotare un volo con dettagli come ID volo, ID passeggero e numero di posto. cancel_booking() annulla una prenotazione aggiornando lo stato della prenotazione. make_payment() processa il pagamento per una prenotazione. bookings.json: Conserva i dettagli delle prenotazioni dei voli, inclusi ID prenotazione, ID volo, ID passeggero, numero di posto e stato. passenger_info.py: Recupera le informazioni dei passeggeri utilizzando la funzione get_passenger_info(), che accede ai dati dal file passengers.json. payment.py: Contiene la logica per il processo di pagamento. Aggiorna lo stato della prenotazione a "pagato" nel file bookings.json una volta che un pagamento è stato effettuato con successo. cancellation.py: Consente agli utenti di annullare una prenotazione e aggiorna lo stato della prenotazione a "cancellato" nel file bookings.json.

"passenger_management" gestisce le informazioni relative ai passeggeri. È composto da cinque file:

passenger_management.py: Contiene le funzioni per aggiungere i passeggeri e aggiornare le loro informazioni di contatto. La funzione add_passenger() crea una nuova voce per il passeggero con dettagli come nome, età e informazioni di contatto. update_contact_info() consente di modificare i dettagli di contatto del passeggero. passengers.json: Conserva i dati dei passeggeri, inclusi ID passeggero, nome, età e informazioni di contatto. booking_history.py: Consente agli utenti di recuperare la cronologia delle prenotazioni di un passeggero utilizzando la funzione get_booking_history(), che accede ai dati dal file bookings.csv. loyalty_status.py: Calcola lo stato di fedeltà del passeggero in base al numero di prenotazioni effettuate utilizzando la funzione calculate_loyalty_status(). Lo stato è determinato dal file bookings.csv. update_contact.py: Simile a passenger_management.py, questo file consente di aggiornare le informazioni di contatto del passeggero.

Il repository "flight_schedule" si occupa degli orari dei voli e della disponibilità. Include cinque file:

flight_schedule.py: Fornisce funzionalità per recuperare i voli disponibili, verificare lo stato di un volo e aggiornare gli orari dei voli. La funzione get_available_flights() restituisce un elenco di voli disponibili per una determinata rotta e data, utilizzando i dati dal file flights.json. get_flight_status() consente di verificare lo stato di un volo specifico. update_flight_schedule() consente agli utenti di modificare l'orario di un volo. flights.json: Contiene dettagli degli orari dei voli, come ID volo, origine, destinazione, data, stato e orario. seat_map.py: Recupera la mappa dei posti per un determinato volo utilizzando la funzione get_seat_map(), che recupera i dati dal file seats.csv. flight_status.py: Simile a flight_schedule.py, questo file verifica lo stato di un volo basandosi sui dati del file flights.json. update_schedule.py: Consente agli utenti di aggiornare l'orario di un volo utilizzando la funzione update_flight_schedule(), modificando i dati nel file flights.json.

Il server è un'applicazione Flask che funge da backend per il nostro sistema aereo. Fornisce endpoint API per gestire la prenotazione dei voli, l'annullamento delle prenotazioni e l'ottenimento dello stato dei voli. Il server utilizza file JSON (bookings.json, passengers.json e flights.json) e interazioni con i repository corrispondenti (flight_booking, passenger_management e flight_schedule) per gestire le prenotazioni e lo stato dei voli.

Il file HTML rappresenta un'interfaccia utente frontend per l'applicazione di prenotazione dei voli. Include un modulo in cui gli utenti possono inserire i dettagli del volo (ad esempio, ID volo, ID passeggero, numero di posto) e un pulsante per prenotare il volo. Quando l'utente invia il modulo di prenotazione o quando la pagina viene caricata, il codice JavaScript interagisce con il server per prenotare un volo o recuperare lo stato di un volo specifico.
