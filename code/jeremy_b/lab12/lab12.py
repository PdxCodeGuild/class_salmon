"""

Author: Jeremy Bush
Project: Programming Boot Camp Lab 12
Version: 3
Date: 6/1/2021

"""


import ATM


atm = ATM.Atm()

print('Welcome to the ATM')
while True:
    command = input('Enter a command: ')
    if command == 'balance':
        balance = atm.check_balance() # call the check_balance() method
        print(f'Your balance is ${balance}')
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? '))
        atm.deposit(amount) # call the deposit(amount) method
        print(f'Deposited $' + f"{ : .2f}".format(amount))
    elif command == 'withdraw':
        amount = float(input('How much would you like ').format())
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
    elif command == 'transactions':
        print("Transaction History:")
        if len(atm.transactions) > 0:
            for transaction in atm.transactions:
                print(transaction)
        else:
            print("No transactions found!")
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('transactions - Print transactions')
        print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')






