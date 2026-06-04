num = int(input("Enter a number: "))

factors = []

for i in range(1, num + 1):
    if num % i == 0:
        factors.append(i)

if len(factors) == 2:
    print(num, "is a Prime Number")
else:
    print(num, "is NOT a Prime Number")
    print("Factors are:", factors)
