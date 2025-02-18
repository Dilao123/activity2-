# task3.py

class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. Current balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Current balance: ${self.balance}")
        else:
            print("Insufficient funds for withdrawal.")

    def display_balance(self):
        print(f"Account balance: ${self.balance}")


account = BankAccount("123456789", "Angelo Dilao", 400)
account.deposit(100)
account.withdraw(50)
account.display_balance()