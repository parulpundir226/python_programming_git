 current_floor = 0
total_floors = 0

while True:
    destination = int(input("Enter destination floor (-1 to stop): "))

    if destination == -1:
        break

    travelled = abs(destination - current_floor)

    print("Floors travelled in this trip:", travelled)

    total_floors += travelled
    current_floor = destination

print("\nTotal floors travelled:", total_floors)
