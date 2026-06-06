employees = (
    ("E101", "Anuj", 92),
    ("E102", "Rahul", 76),
    ("E103", "Priya", 58),
    ("E104", "Neha", 88),
    ("E105", "Amit", 45)
)

# 1. Employees scoring 80 or above
print("Employees scoring 80 or above:")
for emp in employees:
    if emp[2] >= 80:
        print(emp)

# 2. Count employees needing improvement
count = 0
for emp in employees:
    if emp[2] < 60:
        count += 1

print("\nEmployees needing improvement:", count)

# 3. Employee with highest score
highest = employees[0]

for emp in employees:
    if emp[2] > highest[2]:
        highest = emp

print("\nEmployee with highest score:")
print(highest)

# 4. List of employees scoring above 75
high_scorers = []

for emp in employees:
    if emp[2] > 75:
        high_scorers.append(emp[1])

print("\nEmployees scoring above 75:")
print(high_scorers)

# 5. Performance category
print("\nPerformance Categories:")
for emp in employees:
    score = emp[2]

    if score >= 90:
        category = "Excellent"
    elif score >= 75:
        category = "Good"
    elif score >= 60:
        category = "Average"
    else:
        category = "Needs Improvement"

    print(emp[1], "-", category)
