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
    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        self.deposits.append({"amount": amount, "narration": "deposit"})

    def withdrawal(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.withdrawals.append({"amount": amount, "narration": "withdrawal"})
        else:
            print("Insufficient funds!")

    def print_statement(self):
        transactions = self.deposits + self.withdrawals
        for transaction in transactions:
            print(f"{transaction['narration']} - {transaction['amount']}")

    def borrow_loan(self, amount):
        if self.loan_balance == 0 and amount > 100 and len(self.deposits) >= 10 and amount <= sum(
                deposit["amount"] for deposit in self.deposits) / 3:
            self.loan_balance += amount
            print("Loan approved!")
        else:
            print("Loan request denied!")

    def repay_loan(self, amount):
        if self.loan_balance == 0:
            print("No outstanding loan.")
        elif amount >= self.loan_balance:
            self.balance += amount - self.loan_balance
            self.loan_balance = 0
            print("Loan repaid successfully!")
        else:
            self.loan_balance -= amount
            print("Partial loan repayment made.")

    def transfer(self, amount, recipient_account):
        if self.balance >= amount:
            self.balance -= amount
            recipient_account.deposit(amount)
            print("Transfer successful!")
        else:
            print("Insufficient funds for transfer.")

    

  