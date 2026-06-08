employee_id = "EMP2026ANUJ458"

# Count uppercase letters
uppercase_count = 0
for ch in employee_id:
    if ch.isupper():
        uppercase_count += 1

# Count digits and create digit list
digit_count = 0
digit_list = []

for ch in employee_id:
    if ch.isdigit():
        digit_count += 1
        digit_list.append(int(ch))

# Extract joining year and employee name
joining_year = employee_id[3:7]
employee_name = employee_id[7:-3]

# Sum of digits
sum_digits = sum(digit_list)

# Validation
valid = (
    employee_id.startswith("EMP")
    and joining_year.isdigit()
    and len(joining_year) == 4
    and employee_id[-3:].isdigit()
    and len(employee_id[-3:]) == 3
)

# Display output
print("Employee ID:", employee_id)
print("Uppercase Letters:", uppercase_count)
print("Digits:", digit_count)
print("Joining Year:", joining_year)
print("Employee Name:", employee_name)
print("Digit List:", digit_list)
print("Sum of Digits:", sum_digits)

if valid:
    print("ID Status: Valid")
else:
    print("ID Status: Invalid")
