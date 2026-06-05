seats = [1, 0, 1, 1, 0, 0, 1, 1, 1, 0]

# 1. Count booked and available seats
booked = 0
available = 0

for seat in seats:
    if seat == 1:
        booked += 1
    else:
        available += 1

print("Booked Seats:", booked)
print("Available Seats:", available)

# 2. Find the first available seat and stop searching
for i in range(len(seats)):
    if seats[i] == 0:
        print("First Available Seat:", i + 1)
        break

# 3. Create a list of all available seat numbers
available_seats = []

for i in range(len(seats)):
    if seats[i] == 0:
        available_seats.append(i + 1)

print("Available Seat Numbers:", available_seats)

# 4. Check if bus is more than 70% occupied
occupancy = (booked / len(seats)) * 100

print("Occupancy Percentage:", occupancy, "%")

if occupancy > 70:
    print("Bus is more than 70% occupied.")
else:
    print("Bus is not more than 70% occupied.")
