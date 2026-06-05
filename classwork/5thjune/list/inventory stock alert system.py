stock = [25, 5, 0, 12, 3, 18, 0, 30]

print("Out of Stock Products:")
for i in range(len(stock)):
    if stock[i] == 0:
        print("Product", i + 1)

print("\nProducts Needing Restocking (less than 10):")
for i in range(len(stock)):
    if stock[i] < 10:
        print("Product", i + 1, "- Stock:", stock[i])

available_count = 0
for quantity in stock:
    if quantity > 0:
        available_count += 1

print("\nAvailable Products Count:", available_count)

high_stock = []
for quantity in stock:
    if quantity >= 15:
        high_stock.append(quantity)

print("\nProducts with Stock >= 15:")
print(high_stock)
