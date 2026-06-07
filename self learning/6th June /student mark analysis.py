marks = {
    "Aarav": 78,
    "Diya": 92,
    "Rohan": 45,
    "Ishita": 88,
    "Kabir": 56,
    "Meera": 39,
    "Arjun": 95,
    "Saanvi": 67,
    "Vivaan": 82,
    "Anaya": 51
}

# 1. Students scoring 80 or above
print("Students scoring 80 or above:")
for name, mark in marks.items():
    if mark >= 80:
        print(name, mark)

print("\n")

# 2. Count failed students (marks < 40)
failed_count = 0
for mark in marks.values():
    if mark < 40:
        failed_count += 1

print("Number of failed students:", failed_count)
print("\n")

# 3. Highest scorer
topper = max(marks, key=marks.get)
print("Highest scorer:", topper, marks[topper])
print("\n")

# 4. Students scoring between 60 and 75
mid_range = []
for name, mark in marks.items():
    if 60 <= mark <= 75:
        mid_range.append(name)

print("Students scoring between 60 and 75:", mid_range)
print("\n")

# 5. Assign grades
print("Grades:")
for name, mark in marks.items():
    if mark >= 90:
        grade = "A"
    elif 75 <= mark <= 89:
        grade = "B"
    elif 50 <= mark <= 74:
        grade = "C"
    else:
        grade = "F"
    
    print(name, ":", mark, "->", grade)
