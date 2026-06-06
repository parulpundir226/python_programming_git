# Student records stored as tuples
students = (
    ("S101", "Rahul", "Python", 5000),
    ("S102", "Anjali", "Java", 6000),
    ("S103", "Rohan", "Web Development", 5500),
    ("S104", "Priya", "Data Science", 7000),
    ("S105", "Amit", "C++", 4500)
)

# 1. Display all student records
print("All Student Records:")
for student in students:
    print(student)

# 2. Display the first student's details
print("\nFirst Student Details:")
print(students[0])

# 3. Display the last student's details using negative indexing
print("\nLast Student Details:")
print(students[-1])

# 4. Display only Student ID and Name for all students
print("\nStudent ID and Name:")
for student in students:
    print("ID:", student[0], ", Name:", student[1])

# 5. Count the total number of students
print("\nTotal Number of Students:", len(students))

# 6. Check whether a student named 'Rahul' exists
found = False

for student in students:
    if student[1] == "Rahul":
        found = True
        break

if found:
    print("\nRahul exists in the records.")
else:
    print("\nRahul does not exist in the records.")
