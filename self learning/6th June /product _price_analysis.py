prices = {
    "Laptop": 55000,
    "Mouse": 800,
    "Keyboard": 1800,
    "Monitor": 12000,
    "Printer": 9000,
    "Tablet": 28000,
    "Speaker": 3500,
    "Webcam": 2500,
    "Headphones": 4200,
    "Router": 3200
}

# 1. Products costing more than ₹5000
print("Products costing more than ₹5000:")
for product, price in prices.items():
    if price > 5000:
        print(product, price)

print("\n")

# 2. Count products costing less than ₹3000
count_low = 0
for price in prices.values():
    if price < 3000:
        count_low += 1

print("Products costing less than ₹3000:", count_low)
print("\n")

# 3. Most expensive product
max_product = max(prices, key=prices.get)
print("Most expensive product:", max_product, prices[max_product])
print("\n")

# 4. Products between ₹2000 and ₹10000
mid_range = []
for product, price in prices.items():
    if 2000 <= price <= 10000:
        mid_range.append(product)

print("Products between ₹2000 and ₹10000:", mid_range)
print("\n")

# 5. Total value of all products
total_value = sum(prices.values())
print("Total value of all products:", total_value)
