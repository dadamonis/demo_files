from datetime import datetime
from typing import Dict, Optional, List

class Transaction:
    def __init__(self, amount: float, transaction_type: str):
        self.amount = amount
        self.transaction_type = transaction_type
        self.date = datetime.now()

class BankAccount:
    def __init__(self, account_number: str, initial_balance: float = 0.0):
        self.account_number = account_number
        self.balance = initial_balance
        self.transactions: List[Transaction] = []

    def deposit(self, amount: float) -> None:
        self.balance += amount
        self.transactions.append(Transaction(amount, 'Deposit'))
    
    def withdraw(self, amount: float) -> None:
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(Transaction(amount, 'Withdraw'))
        else:
            raise ValueError("Insufficient funds")

    def is_overdrawn(self) -> bool:
        return self.balance < 0

class SavingsAccount(BankAccount):
    def __init__(self, account_number: str, initial_balance: float = 0.0, interest_rate: float = 0.01):
        super().__init__(account_number, initial_balance)
        self.interest_rate = interest_rate

    def apply_interest(self) -> None:
        interest_amount = self.balance * self.interest_rate
        self.deposit(interest_amount)

class Customer:
    def __init__(self, name: str, customer_id: str):
        self.name = name
        self.customer_id = customer_id
        self.accounts: Dict[str, BankAccount] = {}

    def add_account(self, account: BankAccount) -> None:
        self.accounts[account.account_number] = account

    def get_account(self, account_number: str) -> Optional[BankAccount]:
        return self.accounts.get(account_number)

    def get_total_balance(self) -> float:
        return sum(account.balance for account in self.accounts.values())
