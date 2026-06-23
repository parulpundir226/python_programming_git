# Movie Ticket Booking System

movies = {
    "Avengers": {"price": 200, "seats": 50},
    "Spider-Man": {"price": 180, "seats": 40},
    "Batman": {"price": 150, "seats": 30}
}

bookings = []

def display_movies():
    print("\n===== AVAILABLE MOVIES =====")
    for movie, details in movies.items():
        print(
            f"{movie} | Ticket Price: ₹{details['price']} | Available Seats: {details['seats']}"
        )

def book_ticket():
    display_movies()

    movie_name = input("\nEnter movie name: ")

    if movie_name not in movies:
        print("Movie not found!")
        return

    try:
        tickets = int(input("Enter number of tickets: "))
    except ValueError:
        print("Invalid input!")
        return

    if tickets <= 0:
        print("Enter valid number of tickets.")
        return

    if tickets > movies[movie_name]["seats"]:
        print("Not enough seats available!")
        return

    customer_name = input("Enter your name: ")

    total_amount = tickets * movies[movie_name]["price"]

    movies[movie_name]["seats"] -= tickets

    booking = {
        "customer": customer_name,
        "movie": movie_name,
        "tickets": tickets,
        "amount": total_amount
    }

    bookings.append(booking)

    print("\n===== BOOKING SUCCESSFUL =====")
    print("Customer:", customer_name)
    print("Movie:", movie_name)
    print("Tickets:", tickets)
    print("Total Amount: ₹", total_amount)

def view_bookings():
    if not bookings:
        print("\nNo bookings found.")
        return

    print("\n===== ALL BOOKINGS =====")

    for i, booking in enumerate(bookings, start=1):
        print(f"\nBooking {i}")
        print("Customer:", booking["customer"])
        print("Movie:", booking["movie"])
        print("Tickets:", booking["tickets"])
        print("Amount: ₹", booking["amount"])

def cancel_booking():
    customer_name = input("\nEnter customer name: ")

    for booking in bookings:
        if booking["customer"].lower() == customer_name.lower():

            movies[booking["movie"]]["seats"] += booking["tickets"]

            bookings.remove(booking)

            print("Booking cancelled successfully!")
            return

    print("Booking not found.")

def main():
    while True:
        print("\n")
        print("===== MOVIE TICKET BOOKING SYSTEM =====")
        print("1. View Movies")
        print("2. Book Ticket")
        print("3. View Bookings")
        print("4. Cancel Booking")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_movies()

        elif choice == "2":
            book_ticket()

        elif choice == "3":
            view_bookings()

        elif choice == "4":
            cancel_booking()

        elif choice == "5":
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice! Please try again.")

main()
