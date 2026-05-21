# Flight-Booking-System

This is a command-line flight booking system written in Python. It allows users to:

View available flights
Book a single seat per passenger
Cancel a booking
View all passengers and their booking status

The system supports multiple planes and tracks seat availability dynamically.

Features
🧍 Passenger Management
Each passenger is created once per name (shared identity system)
Each passenger can only hold one seat at a time
Passenger data is stored globally during runtime
🛫 Flight Management
Multiple planes supported
Each plane has:
A name
A fixed number of seats
A dynamic list of available seats
🎟 Booking System
Seats are removed from availability when booked
Seats are restored when cancelled
Prevents double booking for the same passenger
❌ Cancellation System
Cancels booking only if seat matches passenger’s current reservation
Restores seat back to the correct plane
How to Run
python your_file_name.py

Make sure you're using Python 3.10+ (for match statement support).
