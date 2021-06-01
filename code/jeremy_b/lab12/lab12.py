"""

Author: Jeremy Bush
Project: Programming Boot Camp Lab 12
Version: 1
Date: 6/1/2021

"""


class Atm:
    def __init__(self):
        self.balance = 0.00

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def check_withdrawal(self, amount):
        return amount < self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def calc_interest(self):
        return round(self.balance * .001, 2)


atm = Atm()

print('Welcome to the ATM')
while True:
    command = input('Enter a command: ')
    if command == 'balance':
        balance = atm.check_balance() # call the check_balance() method
        print(f'Your balance is ${balance}')
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? '))
        atm.deposit(amount) # call the deposit(amount) method
        print(f'Deposited ${amount}')
    elif command == 'withdraw':
        amount = float(input('How much would you like '))
        if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
            atm.withdraw(amount) # call the withdraw(amount) method
            print(f'Withdrew ${amount}')
        else:
            print('Insufficient funds')
    elif command == 'interest':
        amount = atm.calc_interest() # call the calc_interest() method
        print(amount)
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')




