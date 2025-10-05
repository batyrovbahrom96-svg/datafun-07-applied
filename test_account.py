from account import Account

# Create an account with name "John" and balance 100
acct = Account("John", 100.0)

# Print the account name
print("Account name:", acct.name)

# Print the account balance
print("Initial balance:", acct.balance)

# Deposit money
acct.deposit(50.0)
print("Balance after deposit:", acct.balance)

# Withdraw money
acct.withdraw(30.0)
print("Balance after withdrawal:", acct.balance)
