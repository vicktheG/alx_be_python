class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = 0
        return account_balance

    def deposit(self, amount):
        self.account_balance += amount
        # print(f"Deposited: {amount}")
        return account_balance
