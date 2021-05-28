#Lab12 ATM
#A newly created account will default to a balance of 0 and an interest rate of 0.1%. 
#I think this has to do with class tree data types (with initializer) from lecture 28May, commented out below
'''class Tree:
    def __init__(self, data, children=None, parent=None):
        self.data = data
        self.children = children or []
        self.parent = parent

    def add_child(self, data):
        child = Tree(data, parent=self)
        self.children.append(child)'''
#let us try
class ATM:
    def __init__(self, balance = 0, interest_rate = 0.1, amount = 0):#balance always starts 1, interest rate 0.1
        #when you set one of the args for __init__ equal to something this means it is a default (from pete)
        self.balance = balance #arg1
        self.interest_rate = interest_rate #arg2
    #balance is the first function we want to return something directly from __init__
    def get_balance(self):
        #self.balance = balance
        return self.balance
    #deposit is the second function that is not doing the same thing upon initialization
    def deposit(self, amount):
        #we want the balance value to increase
        self.balance += amount
    #check_withdrawal is the third function that is not doing the same thing upon initialization
    def check_withdrawal(self, amount):
        #we want to return true if the withdrawn amount wont make account negative
        if self.balance >= amount:
            return True
    #withdraw is the fourth function that is not doing the same thing upon initialization
    def withdraw(self, amount):
        #we want to decrease the balance by that amount
        self.balance -= amount
    #calc_interest is the fifth function that is not doing the same thing upon initialization
    def calc_interest(self):
        #we want to multiply the balance by the interest rate, not sure what we should do with the earnings
        return self.balance * self.interest_rate
    
    '''balance(self, account):
        balance = ATM(account, balance=self)
        self.balance.append(balance)#I feel like I do not know what this means.
    def interest_rate(self, account):
        interest_rate = ATM(account, interest_rate=self)
        self.interest_rate.append(interest_rate)
    def '''
#implement initilizer
atm = ATM() # create an instance of our class
print('atm variable is ' + str(atm))
print('Welcome to the ATM')
while True:
    command = input('Enter a command: balance, deposit, withdraw, interest, help, exit ')
    if command == 'balance':
        print('command is ' +str(command))
        #print('balance is ' + str(balance))#the variable balance has not been defined yet, here
        #print(atm.balance())
        balance = atm.get_balance() # call the balance() method
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
        #atm.deposit(amount)
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
'''begin = input('hey would you like to start? yes or no?').lower()
if begin == 'yes':
    print(initializer())
else:
    pass

def initializer():'''
    
