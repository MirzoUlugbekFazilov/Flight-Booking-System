class Passenger:

    passengers = []

    def __init__(self, name: str):
        self.name = name
        self.id = None
        Passenger.passengers.append(self)

    def __str__(self):
        if self.id is not None:
            return f"{self.name} → Seat {self.id}"
        return f"{self.name} (no booking yet)"

    @staticmethod
    def get_or_create(name: str):
        for p in Passenger.passengers:
            if p.name == name:
                return p
        return Passenger(name)

    def book(self, plane, seatid: int):

        if seatid not in plane.seats:
            print("Sorry, that seat is not available anymore.")
            return

        if self.id is not None:
            print("You already have a booking. You can only reserve one seat.")
            return

        plane.seats.remove(seatid)
        self.id = seatid
        print(f"All set {self.name}, you're booked on {plane.name}, seat {seatid}.")

    def cancel(self, plane, seatid: int):

        if self.id == seatid:
            plane.seats.append(seatid)
            plane.seats.sort()
            self.id = None
            print(f"Your booking for seat {seatid} has been cancelled.")
        else:
            print("That seat doesn’t match your current booking.")


class Plane:

    planenames = []
    planes = []

    def __init__(self, name: str, seatsnum: int):
        self.seatsnum = seatsnum
        self.name = name
        self.seats = list(range(1, seatsnum + 1))

        Plane.planes.append(self)
        Plane.planenames.append(self.name)

    def __str__(self):
        return f"{self.name} — {len(self.seats)} seats available out of {self.seatsnum}"


def main():

    Plane("UZAirWays", 15)
    Plane("BritishAirWays", 20)

    checker = True

    print("Welcome 👋 Let’s get your flight sorted.")

    while checker:

        print("\nWhat would you like to do?")
        print("1. Book a seat")
        print("2. Cancel a booking")
        print("3. See all passengers")
        print("4. Exit")

        try:
            choice = int(input("Your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        match choice:

            case 1:
                print("\nHere are the available flights:")
                for i, plane in enumerate(Plane.planes):
                    print(f"{i + 1}. {plane}")

                try:
                    sub_choice = int(input("Pick a flight: ")) - 1
                    selected_plane = Plane.planes[sub_choice]
                except:
                    print("That flight selection didn’t work. Try again.")
                    continue

                print(f"\nGood choice — {selected_plane.name}.")
                print(f"These seats are still free: {selected_plane.seats}")

                try:
                    seat = int(input("Which seat would you like? "))
                except ValueError:
                    print("Seat number must be a number.")
                    continue

                name = input("What’s your name? ")
                passenger = Passenger.get_or_create(name)

                passenger.book(selected_plane, seat)

            case 2:
                name = input("Name on the booking: ")
                passenger = Passenger.get_or_create(name)

                try:
                    seat = int(input("Which seat do you want to cancel? "))
                except ValueError:
                    print("Seat number must be valid.")
                    continue

                if passenger.id != seat:
                    print("That seat isn’t linked to your booking.")
                    continue

                for plane in Plane.planes:
                    if passenger.id == seat:
                        passenger.cancel(plane, seat)
                        break

            case 3:
                print("\nPassengers so far:")
                if not Passenger.passengers:
                    print("No one has booked anything yet.")
                else:
                    for p in Passenger.passengers:
                        print(f"- {p}")

            case 4:
                print("Thanks for using the system. Safe travels ✈️")
                checker = False

            case _:
                print("That option doesn’t exist. Try again.")


if __name__ == "__main__":
    main()
