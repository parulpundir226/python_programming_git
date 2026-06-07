books = {
    "Python Basics": 5,
    "Data Structures": 0,
    "Machine Learning": 3,
    "Java Programming": 2,
    "DBMS": 0,
    "Operating Systems": 6,
    "Networking": 4,
    "Cloud Computing": 1,
    "Cyber Security": 0,
    "Web Development": 7
}

# 1. Books that are currently unavailable (0 copies)
print("Unavailable books:")
for book, count in books.items():
    if count == 0:
        print(book)

print("\n")

# 2. Count number of available books (count > 0)
available_count = 0
for count in books.values():
    if count > 0:
        available_count += 1

print("Number of available books:", available_count)
print("\n")

# 3. Book with maximum copies
max_book = max(books, key=books.get)
print("Book with maximum copies:", max_book, books[max_book])
print("\n")

# 4. Books having less than 3 copies
low_stock = []
for book, count in books.items():
    if count < 3:
        low_stock.append(book)

print("Books with less than 3 copies:", low_stock)
print("\n")

# 5. Total number of books available
total = sum(books.values())
print("Total number of books available:", total)
