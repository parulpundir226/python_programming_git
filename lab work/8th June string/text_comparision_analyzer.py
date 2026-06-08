text = "AAABBBCCCDDDAAA"

# 1 & 2. Count occurrences and create frequency dictionary
freq = {}

for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

# 3. Unique characters
unique_chars = list(freq.keys())

# 4. Most frequent character
most_frequent = max(freq, key=freq.get)

# 5. Create compressed output
compressed = ""
count = 1

for i in range(1, len(text)):
    if text[i] == text[i - 1]:
        count += 1
    else:
        compressed += text[i - 1] + str(count)
        count = 1

compressed += text[-1] + str(count)

# 6. Calculate compression ratio
original_length = len(text)
compressed_length = len(compressed)

compression_ratio = (compressed_length / original_length) * 100

# Output
print("Original Text:", text)

print("\nCharacter Frequencies:")
for char, count in freq.items():
    print(char, "->", count)

print("\nUnique Characters:", unique_chars)

print("\nMost Frequent Character:", most_frequent)

print("\nCompressed Output:", compressed)

print("\nOriginal Length:", original_length)
print("Compressed Length:", compressed_length)

print("Compression Ratio:", round(compression_ratio, 2), "%")
