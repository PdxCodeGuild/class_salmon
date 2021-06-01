class ATM:
    def __init__(self, balance=0, int_rate=.001):
        self.balance = balance
        self.int_rate = int_rate

    def check_balance(self):
        return round(self.balance, 2)

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def check_withdrawal(self, amount):
        if (self.balance - amount) >= 0:
            return True

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def calc_interest(self):
        amount = self.balance * self.int_rate
        return round(amount, 2)


list_o_transact = []


def print_transactions(self):
    return list_o_transact


atm = ATM()  # create an instance of our class
print('Welcome to the ATM')
while True:
    command = input('Enter a command or Enter "help" for options:  ')
    if command == 'balance':
        balance = atm.check_balance()  # call the balance() method
        print(f'Your balance is ${balance}')

    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? '))
        atm.deposit(amount)  # call the deposit(amount) method
        print(f'Deposited ${amount}')
        list_o_transact.append(f'Deposited ${amount}')

    elif command == 'withdraw':
        amount = float(input('How much would you like '))
        # call the check_withdrawal(amount) method
        if atm.check_withdrawal(amount):
            atm.withdraw(amount)  # call the withdraw(amount) method
            print(f'Withdrew ${amount}')
            list_o_transact.append(
                f'Withdrew ${amount}')
        else:
            print('Insufficient funds')

    elif command == 'interest':
        amount = atm.calc_interest()  # call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')

    elif command == 'transactions':
        print(list_o_transact)

    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('transactions - see deposits and withdrawals')
        print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')
