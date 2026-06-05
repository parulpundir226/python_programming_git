de = input("Enter a 6-digit code: ")

if len(code) == 6 and code.isdigit():
    first_sum = int(code[0]) + int(code[1]) + int(code[2])
    last_sum = int(code[3]) + int(code[4]) + int(code[5])

    if first_sum == last_sum:
        print("Valid Secret Code")
    else:
        print("Invalid Secret Code")
else:
    print("Please enter exactly 6 digits")
