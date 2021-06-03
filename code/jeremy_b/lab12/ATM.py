"""

Author: Jeremy Bush
Project: Programming Boot Camp Lab 12, ATM Module
Version: 1
Date: 6/1/2021

"""


class Atm:
    def __init__(self):
        self.balance = 0.00
        self.transactions = []

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited ${amount}")

    def check_withdrawal(self, amount):
        return amount < self.balance

    def withdraw(self, amount):
        self.balance -= amount
        self.transactions.append(f"Withdrew ${amount}")

    def calc_interest(self):
        return round(self.balance * .001, 2)