rooms = {
    101: {"type": "Single", "price": 2000},
    102: {"type": "Double", "price": 3500},
    201: {"type": "Suite", "price": 6000}
}

bookings = {}


def load_bookings():
    try:
        file = open("bookings.txt", "r")

        for line in file:
            parts = line.strip().split(" - ")

            if len(parts) == 3:
                room_number = int(parts[0].replace("Room ", ""))
                guest_name = parts[1]
                nights = int(parts[2].split()[0])

                if room_number in rooms:
                    bookings[room_number] = [guest_name, nights]

        file.close()
    except FileNotFoundError:
        pass
    except ValueError:
        pass


def save_bookings():
    file = open("bookings.txt", "w")

    for room_number in bookings:
        guest_name = bookings[room_number][0]
        nights = bookings[room_number][1]
        file.write("Room " + str(room_number) + " - " + guest_name + " - " + str(nights) + " nights\n")

    file.close()


def show_rooms():
    print("\nAvailable rooms:")
    room_found = False

    for room_number in rooms:
        if room_number not in bookings:
            room_type = rooms[room_number]["type"]
            price = rooms[room_number]["price"]
            print("Room", room_number, "-", room_type, "- Rs.", price, "per night")
            room_found = True

    if room_found == False:
        print("No rooms are currently available.")


def book_room():
    guest_name = input("Enter guest name: ").strip()

    if guest_name == "":
        print("Guest name cannot be empty.")
        return

    try:
        room_number = int(input("Enter room number: "))
    except ValueError:
        print("Please enter a room number using digits.")
        return

    if room_number not in rooms:
        print("Room number not found. Please choose 101, 102, or 201.")
        return

    try:
        nights = int(input("Enter number of nights (minimum 1): "))
    except ValueError:
        print("Please enter the number of nights using digits.")
        return

    if nights < 1:
        print("Number of nights must be at least 1.")
        return

    if room_number in bookings:
        old_guest = bookings[room_number][0]
        print("Room", room_number, "is already booked by", old_guest + ". Please choose another room.")
        return

    price = rooms[room_number]["price"]
    amount = price * nights
    gst = round(amount * 0.12)
    total = amount + gst

    bookings[room_number] = [guest_name, nights]
    save_bookings()

    print("Room", room_number, "booked for", guest_name, "|", nights, "night(s)")
    print("Bill:", amount, "+ GST", gst, "= Rs.", total)


def show_bookings():
    print("\nCurrent bookings:")

    if len(bookings) == 0:
        print("There are no bookings.")
    else:
        for room_number in bookings:
            guest_name = bookings[room_number][0]
            nights = bookings[room_number][1]
            price = rooms[room_number]["price"]
            total = price * nights + round(price * nights * 0.12)
            print("Room", room_number, "-", guest_name, "-", nights, "night(s) - Total Rs.", total)


def cancel_booking():
    try:
        room_number = int(input("Enter room number to cancel: "))
    except ValueError:
        print("Please enter a room number using digits.")
        return

    if room_number not in rooms:
        print("Room number not found. Please choose 101, 102, or 201.")
    elif room_number not in bookings:
        print("Room", room_number, "has no booking to cancel.")
    else:
        del bookings[room_number]
        save_bookings()
        print("Booking for room", room_number, "canceled. Room", room_number, "is now available.")


load_bookings()

print("Welcome to the Hotel Room Booking System")

while True:
    print("\n1. View available rooms")
    print("2. Book a room")
    print("3. View current bookings")
    print("4. Cancel a booking")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        show_rooms()
    elif choice == "2":
        book_room()
    elif choice == "3":
        show_bookings()
    elif choice == "4":
        cancel_booking()
    elif choice == "5":
        print("Thank you for using the Hotel Room Booking System.")
        break
    else:
        print("Invalid menu choice. Please enter a number from 1 to 5.")
