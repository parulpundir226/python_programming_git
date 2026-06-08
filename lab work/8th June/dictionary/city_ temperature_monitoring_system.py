# Dictionary storing city temperatures
temperature = {
    "Delhi": 41,
    "Mumbai": 33,
    "Chennai": 37,
    "Kolkata": 39,
    "Bengaluru": 28,
    "Pune": 30,
    "Jaipur": 42,
    "Lucknow": 40,
    "Hyderabad": 35,
    "Ahmedabad": 43
}

# Display cities above 40°C
print("Cities Above 40°C:")
for city, temp in temperature.items():
    if temp > 40:
        print(city)

# Find hottest city
hottest = max(temperature, key=temperature.get)
print("Hottest City:", hottest, "(", temperature[hottest], "°C )")

# Find coolest city
coolest = min(temperature, key=temperature.get)
print("Coolest City:", coolest, "(", temperature[coolest], "°C )")

# Calculate average temperature
avg_temp = sum(temperature.values()) / len(temperature)
print("Average Temperature:", avg_temp)

# Pleasant cities
pleasant = []
for city, temp in temperature.items():
    if temp < 35:
        pleasant.append(city)

print("Pleasant Cities:", pleasant)

# Count cities between 35°C and 40°C
count = 0
for temp in temperature.values():
    if 35 <= temp <= 40:
        count += 1

print("Cities Between 35°C and 40°C:", count)
