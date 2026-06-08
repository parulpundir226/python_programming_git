s = input("Enter a sentence: ")

count = 0

for ch in s:
    if ch.lower() in "aeiou":
        count += 1

print("Total vowels =", count)
