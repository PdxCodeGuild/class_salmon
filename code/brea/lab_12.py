class ATM:
    def __init__(self, balance=0, interest=0.1):
        self.balance = balance
        self.interest = interest
        self.transaction_history = []  

    def check_balance(self):
        return self.balance

    def deposit(self, amount):            
        self.balance += amount
        self.transaction_history.append(f'Deposited {amount}')

    def check_withdrawl(self, amount):
        return True if self.balance - amount >= 0 else False

    def withdrawl(self, amount):
        self.balance -= amount
        self.transaction_balance.append(f'Withdrawl {amount}')
        return self.balance

    def calc_interest(self):
        return self.balance * (self.interest/100)

    def print_transactions(self):
        print(self.transactions)


atm = ATM() # create an instance of our class
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
        if atm.check_withdrawl(amount): # call the check_withdrawal(amount) method
            atm.withdrawl(amount) # call the withdraw(amount) method
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
        print('transactions  -  get transaction history')
    elif command == 'exit':
        break
    elif command == 'transactions':
        print(atm.print_transactions())    
    else:
        print('Command not recognized')