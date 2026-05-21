# ✈️ Flight Booking System (CLI Python Application)

## Video Demo

https://youtu.be/28b2H5DP4qI?si=yTJEj_hmDfLYy_Qu

---

## Overview

This project is a command-line flight booking system built in Python. It simulates a simplified airline reservation workflow where users can interactively browse flights, book seats, cancel reservations, and view all passengers.

The application is fully in-memory, meaning all data exists only during runtime and is reset when the program exits. It is designed as an object-oriented programming exercise focusing on class design, state management, and interaction between multiple objects.

The system supports multiple planes, each with independent seat tracking and availability.

---

## Features

### Passenger Management

The system models passengers using a shared runtime identity system.

- Each passenger is identified by name during a session
- If a name is reused, the same passenger object is retrieved
- Each passenger can only hold one active booking at a time
- Passenger data is not saved after the program ends

This approach simplifies identity handling but assumes that passenger names are unique within a session.

---

### Flight Management

Flights are represented as independent `Plane` objects.

- Multiple planes can exist simultaneously
- Each plane is initialized with a fixed number of seats
- Seats are stored as a dynamic list of available seat numbers
- Each plane manages its own seat availability independently

This ensures that booking on one plane does not affect another.

---

### Booking System

The booking process assigns seats from the selected plane.

- Seats are removed from the plane’s available seat list when booked
- A passenger can only book one seat at a time
- Duplicate bookings are prevented at the passenger level
- Booking confirmation is printed after successful reservation

This ensures consistency between passenger state and seat availability.

---

### Cancellation System

The cancellation system allows users to remove existing bookings.

- A booking can only be cancelled if the seat matches the passenger’s current booking
- The cancelled seat is restored back to the correct plane
- Passenger booking state is reset after cancellation

This ensures that seat availability remains accurate after cancellations.

---

## System Design

The system is built using two core classes:

- `Passenger`: Handles passenger identity and booking state
- `Plane`: Manages flight details and seat availability

Both classes use class-level lists to track active objects during runtime. This design keeps the system simple but introduces global state coupling, which is acceptable for learning purposes but not ideal for production systems.

---

## Limitations

- No persistent storage (data resets when program exits)
- Passenger identity is based on name only (not globally unique)
- Seat ownership is not represented as a separate booking object
- Uses global class lists for tracking passengers and planes
- Minimal error handling in some user input paths

---

## How to Run

```bash
python your_file_name.py
