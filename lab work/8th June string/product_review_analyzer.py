review = "This product is excellent excellent excellent and very useful"

# 1. Split words
words = review.split()

# 2. Total words
total_words = len(words)

# 3. Word frequencies (dictionary)
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

# 4. Most frequent word
most_frequent = max(freq, key=freq.get)

# 5. Words appearing only once
once_words = [word for word, count in freq.items() if count == 1]

# 6. Words having more than 5 characters
long_words = [word for word in words if len(word) > 5]

# 7. Reverse order of words
reversed_words = words[::-1]

# 8. Unique words list
unique_words = list(freq.keys())

# Output
print("Total Words:", total_words)

print("\nWord Frequencies:")
for word, count in freq.items():
    print(word, "->", count)

print("\nMost Frequent Word:", most_frequent)

print("Words Appearing Once:", once_words)

print("Words Longer Than 5 Characters:", long_words)

print("Reversed Words:", reversed_words)

print("Unique Words:", unique_words)
