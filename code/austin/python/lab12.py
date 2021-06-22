class ATM:
    def __init__(self, balance=0, interest=.001):
        self.balance = balance
        self.interest = interest
        self.transaction = []
    def check_balance(self):# returns the account balance
        return self.balance
    def deposit(self,amount): #deposits the given amount in the account
        self.balance = self.balance + amount
        self.transaction.append(f'user deposited ${amount}')
        print(self.transaction)
        return amount
    def check_withdrawal(self,amount): #returns true if the withdrawn amount won't put the account in the negative
        if self.balance >= amount:
            return True
        else:
            return False
    def withdraw(self,amount): #withdraws the amount from the account and returns it
        self.balance -= amount
        self.transaction.append(f'user withdrew ${amount}')
        print(self.transaction)
        return amount
    def calc_interest(self): #returns the amount of interest calculated on the account
        interest_accrued = self.balance * self.interest
        return interest_accrued
    def print_transactions(self):
        return self.transaction
atm = ATM() # create an instance of our class
print('Welcome to the ATM')
print('Available commands:')
print('balance  - get the current balance')
print('deposit  - deposit money')
print('withdraw - withdraw money')
print('interest - accumulate interest')
print('transactions - see a list of transactions')
print('exit     - exit the program')
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
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('exit     - exit the program')
    elif command == 'transactions':
        print(atm.print_transactions())
    elif command == 'exit':
        break
    else:
        print('Command not recognized')