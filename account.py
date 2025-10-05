# account.py
"""Account class definition."""

class Account:
    """Account class for a bank account."""

    def __init__(self, name, balance):
        """Initialize an Account object."""
        self.name = name
        
        if balance > 0.0:
            self.balance = balance
        else:
            self.balance = 0.0

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0.0:
            self.balance += amount

    def withdraw(self, amount):
        """Withdraw money from the account if sufficient balance exists."""
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("Withdrawal amount exceeded account balance.")