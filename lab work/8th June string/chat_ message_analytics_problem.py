message = "Python is awesome and Python is easy to learn"

# 1. Count total characters
total_characters = len(message)

# 2. Count total words
words = message.split()
total_words = len(words)

# 3. Find longest word
longest_word = max(words, key=len)

# 4. Find shortest word
shortest_word = min(words, key=len)

# 5. Count occurrences of "Python"
python_count = words.count("Python")

# 6. Words having more than 4 characters
long_words = [word for word in words if len(word) > 4]

# 7. Words starting with a vowel
vowels_start = [word for word in words if word[0].lower() in "aeiou"]

# 8. Count vowels and consonants
vowel_count = 0
consonant_count = 0

for ch in message:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowel_count += 1
        else:
            consonant_count += 1

# Output
print("Message:", message)

print("\nTotal Characters:", total_characters)
print("Total Words:", total_words)

print("\nLongest Word:", longest_word)
print("Shortest Word:", shortest_word)

print("\nOccurrences of Python:", python_count)

print("\nWords Longer Than 4 Characters:", long_words)

print("\nWords Starting With a Vowel:", vowels_start)

print("\nVowels:", vowel_count)
print("Consonants:", consonant_count)
