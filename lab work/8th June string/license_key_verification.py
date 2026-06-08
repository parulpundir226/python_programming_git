license_key = "ABCD-EFGH-IJKL-MNOP"

# 1 & 6. Create list of groups
groups = license_key.split("-")

# Verify number of groups
num_groups = len(groups)

# 2. Verify each group contains exactly 4 characters
valid_groups = True
for group in groups:
    if len(group) != 4:
        valid_groups = False
        break

# 3. Count total letters
merged_key = license_key.replace("-", "")
total_letters = 0

for ch in merged_key:
    if ch.isalpha():
        total_letters += 1

# 4. Count vowels
vowels = "AEIOUaeiou"
vowel_count = 0

for ch in merged_key:
    if ch in vowels:
        vowel_count += 1

# 7. Check key validity
if num_groups == 4 and valid_groups:
    status = "Valid"
else:
    status = "Invalid"

# Output
print("License Key:", license_key)

print("\nGroups:", groups)
print("Number of Groups:", num_groups)

print("\nTotal Letters:", total_letters)
print("Total Vowels:", vowel_count)

print("\nMerged Key:", merged_key)

print("\nLicense Key Status:", status)
