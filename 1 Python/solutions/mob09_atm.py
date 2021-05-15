

class ATM:
    
    def __init__(self, balance, interest_rate):
        # initialize our class with a balance of 0 and an interest rate of 0.1
        self.balance = balance
        self.interest_rate = interest_rate
        self.transactions = []
        
    
    def get_balance(self):
        # return the account balance
        return self.balance
    
    def deposit(self, amount):
        # add the given amount to the balance
        self.balance += amount
        self.transactions.append(f'User deposited ${amount}')
        if len(self.transactions)%5 == 0:
            self.deposit_interest()
    
    def check_withdrawal(self, amount):
        # returns true if the withdrawn amount won't put the account in the negative, false otherwise
        if amount <= self.balance:
            return True
        else:
            return False
    
    def withdraw(self, amount):
        # removes the given amount from the balance and returns it
        self.balance -= amount
        self.transactions.append(f'User withdrew ${amount}')
        if len(self.transactions)%5 == 0:
            self.deposit_interest()
    
    def deposit_interest(self):
        # calculate the amount of interest accumulated and add it to our balance
        # return the amount of interest added
        # calculate the interest by multiplying the interest rate by the balance
        interest = self.interest_rate*self.balance
        self.balance += interest
        self.balance = round(self.balance, 2)
        self.transactions.append(f'Deposited interest ${interest}')
        return interest
    
    def print_transactions(self):
        for i in range(len(self.transactions)):
            print(self.transactions[i])
    

    def __str__(self):
        return f'ATM (balance {self.balance}, interest rate {self.interest_rate})'


atm = ATM(0, 0.1) # create an instance of our class



# calling the __str__ of the list class
# nums = [1, 2, 3]
# print(nums)
# nums_str = str(nums)
# print(nums_str)
# print(nums_str[0])


# calling the __str__ of the atm class
# atm_str = str(atm)
# print(atm_str)

# atm_str = atm.__str__()
# print(atm_str)

# print(atm)

# exit()


# print(atm.balance) # 0
# print(atm.interest_rate) # 0.1
print('Welcome to the ATM')
while True:
    command = input('Enter a command: ')
    if command == 'balance':
        balance = atm.get_balance() # call the get_balance() method
        print(f'Your balance is ${balance}')
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? $'))
        atm.deposit(amount) # call the deposit(amount) method
        print(f'Deposited ${amount}')
    elif command == 'withdraw':
        amount = float(input('How much would you like to withdraw? $'))
        if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
            atm.withdraw(amount) # call the withdraw(amount) method
            print(f'Withdrew ${amount}')
        else:
            print('Insufficient funds')
    elif command == 'interest':
        amount = atm.deposit_interest() # call the deposit_interest() method
        print(f'Deposited ${amount} in interest')
    elif command == 'transactions':
        atm.print_transactions()
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