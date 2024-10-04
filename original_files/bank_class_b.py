class BankAccount:
    def __init__(self, initial_balance: float = 0.0):
        """
        Initialize the bank account with an initial balance.
        :param initial_balance: Initial balance of the account.
        """
        self.balance = initial_balance

    def deposit(self, amount: float) -> None:
        """
        Deposit a specified amount into the account.
        :param amount: Amount to be deposited.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """
        Withdraw a specified amount from the account.
        :param amount: Amount to be withdrawn.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

    def is_overdrawn(self) -> bool:
        """
        Check if the account is overdrawn.
        :return: True if the account is overdrawn, False otherwise.
        """
        return self.balance < 0
