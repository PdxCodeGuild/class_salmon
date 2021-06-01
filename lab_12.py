import math

class ATM:
    def __init__(self, balance=0, interest=0.1):
        self.balance = balance
        self.interest = interest
        self.transactions = []
    def check_balance(self):
        return {self.balance}
    def deposit(self, ammount):
        self.balance += ammount
        self.transactions.append(f'User deposited {ammount}.')
        return {self.balance}
    def check_withdrawal(self, ammount):
        if self.balance - ammount >= 0:
            return True
        else:
            return False
    def withdraw(self, ammount):
        self.balance -= ammount
        self.transactions.append(f'User withdrew {ammount}.')
        return self.balance
    def calc_interest(self):
        acc_interest = self.balance * (self.interest/100)
        return acc_interest
    def print_transactions(self):
        string = f''
        for i in self.transactions:
            string += i + '\n'
        return string.strip()


atm = ATM() # create an instance of our class
print('Welcome to the ATM')
while True:
    command = input('Enter a command: ').lower()
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
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')
    elif command == 'transactions':
        print(atm.print_transactions())
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('transactions - get transaction history')
        print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')
        
