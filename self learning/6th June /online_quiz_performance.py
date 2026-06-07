quiz_scores = {
    "S001": 18,
    "S002": 12,
    "S003": 9,
    "S004": 20,
    "S005": 14,
    "S006": 7,
    "S007": 16,
    "S008": 10,
    "S009": 19,
    "S010": 13
}

# 1. Students scoring 15 or above
print("Students scoring 15 or above:")
for sid, score in quiz_scores.items():
    if score >= 15:
        print(sid, score)

print("\n")

# 2. Count students scoring below 10
below_10 = 0
for score in quiz_scores.values():
    if score < 10:
        below_10 += 1

print("Students scoring below 10:", below_10)
print("\n")

# 3. Top performer
topper = max(quiz_scores, key=quiz_scores.get)
print("Top performer:", topper, quiz_scores[topper])
print("\n")

# 4. Students who passed (>= 10)
passed = []
for sid, score in quiz_scores.items():
    if score >= 10:
        passed.append(sid)

print("Students who passed:", passed)
print("\n")

# 5. Class average
total = sum(quiz_scores.values())
average = total / len(quiz_scores)

print("Class average:", average)
