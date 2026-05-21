# Flight-Booking-System

A command-line application that simulates a basic airline reservation system. Users can browse flights, book a single seat per passenger, cancel bookings, and view all registered passengers.

The system runs entirely in memory and supports multiple planes with independent seat tracking.


## Features

### Passenger Management
- Each passenger is uniquely identified by name within a single runtime session
- One active booking per passenger at a time
- Passenger data persists only while the program is running

### Flight Management
- Multiple planes supported simultaneously
- Each plane has a fixed seat capacity
- Seat availability updates dynamically as bookings and cancellations occur

### Booking System
- Seats are allocated from the available pool per plane
- Prevents duplicate bookings per passenger
- Enforces single-seat-per-passenger rule

### Cancellation System
- Cancels only valid existing bookings
- Restores seat back to the correct plane’s availability list

---

## How to Run

```bash
python your_file_name.py
