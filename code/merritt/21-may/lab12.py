class ATM:
    def __init__(self, balance=0, interest_rate=.001):
        self.__balance = balance
        self.__interest_rate = interest_rate
        self.__transactions = []

    def check_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount
        self.__transactions.append(f"Deposit of ${amount}: New balance ${self.__balance}")

    def check_withdrawl(self, amount):
        # if self.__balance >= amount:
        #     return True
        # return False

        # return True if self.__balance >= amount else False

        return self.__balance >= amount

    def withdrawl(self, amount):
        # if self.__check_withdrawl(amount):
        #     self.__balance -= amount
        # else:
        #     print("Insufficient Funds")
        #     self.__balance -= amount
        #     self.__balance -= 35
        #     # raise ValueError("Insufficient funds!")


        self.__balance -= amount
        self.__transactions.append(f"Withdrawl of ${amount}: New balance ${self.__balance}")

    def calc_interest(self):
        return self.__balance * self.__interest_rate

    def print_transactions(self):
        # print(self.__transactions)

        # for tran in self.__transactions:
        #     print(tran)

        print("\n".join(self.__transactions))


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
    elif command == 'transactions':
        atm.print_transactions()
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('transactions - print transaction history')
        print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')