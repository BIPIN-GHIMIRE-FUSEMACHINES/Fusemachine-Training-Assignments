'''
Build a Python class to represent a simple banking system. Create a class for a
BankAccount, and another for Customer. The BankAccount class should have a
constructor to initialize the account details (account number, balance, account type).
The Customer class should have a constructor to set the customer's details (name,
age, address) and create a BankAccount object for each customer. Implement a
destructor for both classes to display a message when objects are destroyed.
'''

class BankAccount:
    def __init__(self, account_number, balance, account_type):
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type

    def __del__(self):
        print(f"Bank account {self.account_number} of type {self.account_type} is being closed.")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} to account {self.account_number}. New balance: {self.balance}")
        else:
            print("Invalid deposit amount. Amount should be greater than 0.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} from account {self.account_number}. New balance: {self.balance}")
        else:
            print("Invalid withdrawal amount. Either amount is greater than balance or negative.")

    def get_balance(self):
        return self.balance


class Customer:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        self.bank_accounts = []

    def __del__(self):
        print(f"Customer {self.name} is no longer our customer.")

    def create_bank_account(self, account_number, balance, account_type):
        account = BankAccount(account_number, balance, account_type)
        self.bank_accounts.append(account)
        print(f"Bank account {account_number} of type {account_type} created for customer {self.name}.")

    def get_all_accounts(self):
        return self.bank_accounts


# Example Usage:
if __name__ == "__main__":
    # Creating a customer
    customer1 = Customer("Bipin Ghimire", 23, "Battisputali, Kathmandu")
    customer1.create_bank_account("123456789", 1000, "Savings")
    customer1.create_bank_account("987654321", 5000, "Checking")

    # Accessing the customer's accounts
    accounts = customer1.get_all_accounts()
    for account in accounts:
        print(f"Account Number: {account.account_number}, Balance: {account.get_balance()}, Type: {account.account_type}")

    # Depositing and withdrawing from accounts
    accounts[0].deposit(500)
    accounts[1].withdraw(1000)

    # Deleting the customer (which will also delete the associated bank accounts)
    del customer1
