# Dictionary storing player runs
runs = {
    "Virat": 645,
    "Rohit": 512,
    "Gill": 698,
    "Rahul": 435,
    "Hardik": 278,
    "Pant": 534,
    "Surya": 389,
    "Jadeja": 301,
    "Iyer": 455,
    "KL": 410
}

# Display players scoring more than 500 runs
print("Players Scoring More Than 500 Runs:")
for player, run in runs.items():
    if run > 500:
        print(player)

# Find Orange Cap winner
orange_cap = max(runs, key=runs.get)
print("Orange Cap Winner:", orange_cap, "(", runs[orange_cap], ")")

# Find lowest scorer
lowest = min(runs, key=runs.get)
print("Lowest Scorer:", lowest, "(", runs[lowest], ")")

# Calculate total runs
total_runs = sum(runs.values())
print("Total Tournament Runs:", total_runs)

# Players scoring below 400
below_400 = []
for player, run in runs.items():
    if run < 400:
        below_400.append(player)

print("Players Scoring Below 400:", below_400)

# Count players between 400 and 600 runs
count = 0
for run in runs.values():
    if 400 <= run <= 600:
        count += 1

print("Players Between 400 and 600 Runs:", count)
