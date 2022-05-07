# Flight Booking

The flight booking database contains the initials data of the users and bookings.

## Install Instruction 📦
### Getting Start
1. Go to the directory and install the required packages
  ```python
  pip install -r requirements.txt
  ```
  
2. Go to the directory and create "sample.db" using schema commands in a file
  ```python
  sqlite3 flight.db < db.schema
  ```
  
3. Open the database file with the sqlite command line utility
  ```python
  sqlite3 flight.db
  ```
  
4. Import the data from csv to the database file
  ```python
  sqlite> .mode csv
  sqlite> .import data/users.csv users
  sqlite> .import data/flight_bookings.csv flight_bookings
  ```
  
5. Run the application
  ```python
  python main.py
  ```
## Web Service API
- [Flight Booking APIs documentation](https://abounk.github.io/flight-booking/#/document)

## UML Diagrams
- [UML Diagrams](https://abounk.github.io/flight-booking/#/?id=project-description)

