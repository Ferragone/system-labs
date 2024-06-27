class Customer:
    def __init__(self, account):
        self.account = account

class Account:
    def __init__(self, balance):
        self.balance = balance

class Bank:
    def __init__(self, customer):
        self.customer = customer

    def get_balance(self):
        return self.customer.account.balance

# Приклад використання (без ланцюжка викликів)
bank = Bank(Customer(Account(1000)))
balance = bank.get_balance()
print(f"The balance is: {balance}")