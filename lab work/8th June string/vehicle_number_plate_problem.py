plate = "MH12AB4589"

# 1. Extract parts
state_code = plate[0:2]
district_code = plate[2:4]
series = plate[4:6]
vehicle_number = plate[6:10]

# 5. Count letters and digits
letters = 0
digits = 0

for ch in plate:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1

# 6. Validation rules
valid = (
    state_code.isalpha() and len(state_code) == 2 and
    district_code.isdigit() and len(district_code) == 2 and
    series.isalpha() and len(series) == 2 and
    vehicle_number.isdigit() and len(vehicle_number) == 4
)

# 7. Output
print("Vehicle Number:", plate)

print("State Code:", state_code)
print("District Code:", district_code)
print("Series:", series)
print("Vehicle Number:", vehicle_number)

print("\nTotal Letters:", letters)
print("Total Digits:", digits)

print("\nVehicle Number Status:", "Valid" if valid else "Invalid")
