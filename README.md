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

## UML Diagrams

- Domain model
  ![png](https://user-images.githubusercontent.com/73059738/165601241-bfd296d1-a660-4b6c-b4f4-1aaee9843e2c.png)

- Package Diagram
  ![package_diagram](https://user-images.githubusercontent.com/73059738/165601844-e7037b1c-69ed-4f9c-b77f-71153cd0be73.png)

- Class Diagram
  ![class_diagram](https://user-images.githubusercontent.com/73059738/165601425-4023bb82-503e-47cb-a3e0-19633fd1bcd1.png)
