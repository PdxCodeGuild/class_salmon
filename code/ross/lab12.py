class ATM:
    # this initializes the class
    def __init__(self):
        self.__balance = 0
        self.transactions = []

    # this returns the balance in the account
    def check_balance(self):
        # print(balance)
        return self.__balance

    # this allow user to deposit to their account
    def deposit(self, amount):
        self.list_transactions(f"User made a deposit of ${amount}")
        self.__balance += amount


    # returns true if the withdrawn amount won't put the account in the negative
    def check_withdrawal(self, amount):
        if amount >= self.__balance:
            return False
        else:
            return True

    # this allows user to withdraw from their account
    def withdraw(self, amount):
        self.list_transactions(f"User made a withdrawal of ${amount}")
        self.__balance -= amount

    # this allows user to calculate the interest earned on the account
    def calc_interest(self):
        interest = self.__balance * .001
        return interest

    # this method compiles a list of transactions
    def list_transactions(self, transaction):
        self.transactions.append(transaction)

    # this method compiles and prints a list of the users transactions
    def print_transactions(self):
        return self.transactions

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
        print('print - display list of all transactions')
        print('exit     - exit the program')
    elif command == 'print':
        print(atm.print_transactions())
    elif command == 'exit':
        break
    else:
        print('Command not recognized')