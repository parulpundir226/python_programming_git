# Dictionary storing employee performance
performance = {
    "EMP101": 92,
    "EMP102": 78,
    "EMP103": 45,
    "EMP104": 88,
    "EMP105": 97,
    "EMP106": 56,
    "EMP107": 81,
    "EMP108": 64,
    "EMP109": 39,
    "EMP110": 73
}

# Display employees scoring above 80
print("Employees Scoring Above 80:")
for emp, score in performance.items():
    if score > 80:
        print(emp)

# Count employees needing improvement
improvement = 0
for score in performance.values():
    if score < 60:
        improvement += 1

print("Employees Needing Improvement:", improvement)

# Find top performer
top = max(performance, key=performance.get)
print("Top Performer:", top, "(", performance[top], ")")

# Calculate average score
average = sum(performance.values()) / len(performance)
print("Average Score:", average)

# Categorize employees
excellent = []
good = []
average_list = []
poor = []

for emp, score in performance.items():
    if score >= 90:
        excellent.append(emp)
    elif score >= 75:
        good.append(emp)
    elif score >= 60:
        average_list.append(emp)
    else:
        poor.append(emp)

print("Excellent:", excellent)
print("Good:", good)
print("Average:", average_list)
print("Poor:", poor)e
