num = input("Enter a number: ")

i = 1

# Increasing part
while i < len(num) and num[i] > num[i - 1]:
    i += 1

# Peak cannot be first or last digit
if i == 1 or i == len(num):
    print("Not a Mountain Number")
else:
    # Decreasing part
    while i < len(num) and num[i] < num[i - 1]:
        i += 1

    if i == len(num):
        print("
