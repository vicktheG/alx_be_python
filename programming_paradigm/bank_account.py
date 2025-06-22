class BankAccount:
    """
    A simple bank account class that demonstrates OOP principles.

    This class encapsulates banking operations including deposits,
    withdrawals, and balance inquiries.
    """

    def __init__(self, initial_balance=0):
        """
        Initialize a new bank account.

        Args:
            initial_balance (float): Starting balance for the account. Defaults to 0.
        """
        self.account_balance = float(initial_balance)

    def deposit(self, amount):
        """
        Deposit money into the account.

        Args:
            amount (float): Amount to deposit (must be positive)
        """
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw money from the account.

        Args:
            amount (float): Amount to withdraw

        Returns:
            bool: True if withdrawal successful, False if insufficient funds
        """
        if amount > self.account_balance:
            return False
        elif amount > 0:
            self.account_balance -= amount
            return True
        else:
            print("Withdrawal amount must be positive.")
            return False

    def display_balance(self):
        """
        Display the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.account_balance:.2f}")

    def get_balance(self):
        """
        Get the current balance (useful for testing or other operations).

        Returns:
            float: Current account balance
        """
        return self.account_balance
