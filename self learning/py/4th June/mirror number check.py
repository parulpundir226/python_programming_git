num = input("Enter a number: ")

length = len(num)

if length % 2 != 0:
    print("Number must have an even number of digits.")
else:
    half = length // 2

    left_half = num[:half]
    right_half = num[half:]

    if left_half == right_half:
        print("Mirror Number")
    else:
        print("Not a Mirror Number")
