from person import Person
from my_date import Date
from money import Money
import random


class BankAccount:
    def __init__(self, user, created_at, balance, account_id):
        self.user = user
        self.created_at = created_at
        self.balance = balance
        self.account_id = account_id

    def __repr__(self):
        return "User: {}\nCreated at: {}\nBalance: {}\nAccount id: {}".format(self.user, self.created_at, self.balance, self.account_id)

    def deposit(self, p, n):
        return Money(self.balance.currency, round(self.balance.amount * ((1 + p / 100) ** n), 2))

    def withdraw(self, amount):
        if amount > 0:
            if self.balance.amount >= amount:
                self.balance.amount -= amount
                print(f"Withdrawal of {amount} {self.balance.currency} successful. New balance: {self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount. Amount must be greater than 0.")




def generate_unique_number(start=1000000, end=9999999):  # User-ի համար եզակի id գեներացնելու համար
    numbers = set()
    while True:
        num = random.randint(start, end)
        if num not in numbers:
            return num
        numbers.add(num)


user = Person("Amaras", "Arshakyan", 30, "Male", "Amaras@gmail.com")
created_at = Date(2023, 7, 15)
balance = Money("AMD", 500)

account_id = generate_unique_number()
my_account = BankAccount(user, created_at, balance, account_id)
print(my_account.withdraw(200))
print(my_account.deposit(15, 20))
