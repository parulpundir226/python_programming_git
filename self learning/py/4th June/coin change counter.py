amount = int(input("Enter amount: ₹"))

notes_500 = amount // 500
amount %= 500

notes_200 = amount // 200
amount %= 200

notes_100 = amount // 100
amount %= 100

notes_50 = amount // 50
amount %= 50

notes_20 = amount // 20
amount %= 20

notes_10 = amount // 10
amount %= 10

print("₹500 notes:", notes_500)
print("₹200 notes:", notes_200)
print("₹100 notes:", notes_100)
print("₹50 notes:", notes_50)
print("₹20 notes:", notes_20)
print("₹10 notes:", notes_10)
