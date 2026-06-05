transactions = [5000, -2000, 3000, -1000, -500, 7000]

# 1. Calculate current balance
balance = 0

for transaction in transactions:
    balance += transaction

print("Current Balance:", balance)

# 2. Count total deposits and withdrawals
deposit_count = 0
withdrawal_count = 0

for transaction in transactions:
    if transaction > 0:
        deposit_count += 1
    else:
        withdrawal_count += 1

print("Total Deposits:", deposit_count)
print("Total Withdrawals:", withdrawal_count)

# 3. Find largest deposit and largest withdrawal
largest_deposit = transactions[0]
largest_withdrawal = transactions[1]

for transaction in transactions:
    if transaction > 0 and transaction > largest_deposit:
        largest_deposit = transaction

    if transaction < 0 and transaction < largest_withdrawal:
        largest_withdrawal = transaction

print("Largest Deposit:", largest_deposit)
print("Largest Withdrawal:", largest_withdrawal)

# 4. Create separate lists for deposits and withdrawals
deposits = []
withdrawals = []

for transaction in transactions:
    if transaction > 0:
        deposits.append(transaction)
    else:
        withdrawals.append(transaction)

print("Deposits:", deposits)
print("Withdrawals:", withdrawals)
