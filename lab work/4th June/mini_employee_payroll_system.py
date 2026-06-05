name = input("Enter Employee Name: ")
basic_salary = float(input("Enter Basic Salary: ₹"))

hra = basic_salary * 0.20
da = basic_salary * 0.10
gross_salary = basic_salary + hra + da

print("\n----- Employee Payroll -----")
print("Employee Name:", name)
print("Basic Salary: ₹", basic_salary)
print("HRA: ₹", hra)
print("DA: ₹", da)
print("Gross Salary: ₹", gross_salary)
