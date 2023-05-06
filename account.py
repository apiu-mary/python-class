class Account:
    bank_name = "Unknown"
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return f"made a bank deposit of {amount} in the account.your balance is {self.balance}."
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrew {amount} from the account. New balance is {self.balance}."
        else:
            return "Insufficient balance to withdraw."
    def check_balance(self):
        return f"Current balance in the account is {self.balance}."