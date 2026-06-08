# Dictionary storing electricity consumption
units = {
    "House101": 320,
    "House102": 180,
    "House103": 510,
    "House104": 275,
    "House105": 150,
    "House106": 430,
    "House107": 220,
    "House108": 390,
    "House109": 145,
    "House110": 600
}

# Display houses consuming more than 400 units
print("Houses Consuming More Than 400 Units:")
for house, unit in units.items():
    if unit > 400:
        print(house)

# Find highest consumption
highest = max(units, key=units.get)
print("Highest Consumption:", highest, "(", units[highest], "units )")

# Find lowest consumption
lowest = min(units, key=units.get)
print("Lowest Consumption:", lowest, "(", units[lowest], "units )")

# Calculate total units consumed
total_units = sum(units.values())
print("Total Units Consumed:", total_units)

# Categorize houses
low = []
medium = []
high = []

for house, unit in units.items():
    if unit < 200:
        low.append(house)
    elif 200 <= unit <= 400:
        medium.append(house)
    else:
        high.append(house)

print("Low Consumption:", low)
print("Medium Consumption:", medium)
print("High Consumption:", high)

# Count houses eligible for energy-saving campaign
campaign = 0
for unit in units.values():
    if unit > 300:
        campaign += 1

print("Eligible for Energy-Saving Campaign:", campaign)
