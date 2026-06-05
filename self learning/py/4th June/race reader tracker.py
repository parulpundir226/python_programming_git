n = int(input("Enter number of racers: "))

lap_times = []

for i in range(n):
    time = float(input(f"Enter lap time of Racer {i + 1}: "))
    lap_times.append(time)

fastest_time = min(lap_times)
slowest_time = max(lap_times)

fastest_position = lap_times.index(fastest_time) + 1
slowest_position = lap_times.index(slowest_time) + 1

difference = slowest_time - fastest_time

print("\nFastest Racer Position:", fastest_position)
print("Slowest Racer Position:", slowest_position)
print("Difference in Lap Time:", difference)
