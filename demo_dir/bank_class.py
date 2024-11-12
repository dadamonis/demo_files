from datetime import datetime

class Transaction:
    def __init__(self, amount, transaction_type):
        self.amount = amount
        self.transaction_type = transaction_type
        self.date = datetime.now()

class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(Transaction(amount, 'Deposit'))

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(Transaction(amount, 'Withdraw'))
        else:
            raise ValueError("Insufficient funds")

    def is_overdrawn(self):
        return self.balance < 0

class SavingsAccount(BankAccount):
    def __init__(self, account_number, initial_balance=0, interest_rate=0.01):
        super().__init__(account_number, initial_balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest_amount = self.balance * self.interest_rate
        self.deposit(interest_amount)

class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account

    def get_account(self, account_number):
        return self.accounts.get(account_number)

    def get_total_balance(self):
        return sum(account.balance for account in self.accounts.values())