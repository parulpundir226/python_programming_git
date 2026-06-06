bookings = (
    ("P101", "Delhi", "Confirmed"),
    ("P102", "Mumbai", "Waiting"),
    ("P103", "Delhi", "Confirmed"),
    ("P104", "Chennai", "Cancelled"),
    ("P105", "Mumbai", "Confirmed"),
    ("P106", "Delhi", "Waiting")
)

# 1. Display all confirmed bookings
print("Confirmed Passengers:")
for booking in bookings:
    if booking[2] == "Confirmed":
        print(booking)

# 2. Count passengers travelling to Delhi
delhi_count = 0

for booking in bookings:
    if booking[1] == "Delhi":
        delhi_count += 1

print("\nPassengers travelling to Delhi:", delhi_count)

# 3. Count booking statuses
confirmed = 0
waiting = 0
cancelled = 0

for booking in bookings:
    if booking[2] == "Confirmed":
        confirmed += 1
    elif booking[2] == "Waiting":
        waiting += 1
    elif booking[2] == "Cancelled":
        cancelled += 1

print("\nConfirmed Bookings:", confirmed)
print("Waiting Bookings:", waiting)
print("Cancelled Bookings:", cancelled)

# 4. List of passenger IDs with Waiting status
waiting_passengers = []

for booking in bookings:
    if booking[2] == "Waiting":
        waiting_passengers.append(booking[0])

print("\nPassengers with Waiting Status:")
print(waiting_passengers)

# 5. Destination with highest number of bookings
destination_count = {}

for booking in bookings:
    destination = booking[1]

    if destination in destination_count:
        destination_count[destination] += 1
    else:
        destination_count[destination] = 1

highest_destination = max(destination_count, key=destination_count.get)

print("\nDestination with Highest Bookings:", highest_destination)
