### Procedural/Imperative ###

# balance = 0
# interest_rate = 0.1

# balance += 100

# print(balance)

# balance -= 50

# print(balance)





### Declarative/Logical ###

# <bank>
#     <account name="Merritt" type="checking" balance="50">
#     <account name="Nick" type="savings" balance="250">
# </bank>





### Object Oriented ###

# class Account:
#     def __init__(self, initial_balance=0, interest_rate=0.1):
#         self.balance = initial_balance
#         self.interest_rate = interest_rate

#     def check_balance(self):
#         return self.balance

#     def deposit(self, amount):
#         self.balance += amount

#     def check_withdrawl(self, amount):
#         if self.balance >= amount:
#             return True
#         else:
#             return False
    
#     def withdraw(self, amount):
#         if self.check_withdrawl(amount):
#             self.balance -= amount
#         else:
#             print("Insufficient Funds!")

#     def calc_interest(self):
#         return self.balance * self.interest_rate

# atm = Account()
# atm.deposit(100)
# print(atm.check_balance())
# atm.withdraw(50)
# print(atm.check_balance())





### Functional (Basic) ###

# def initialize_account(initial_balance=0, interest_rate=0.1):
#     return {
#         'balance': initial_balance,
#         'interest_rate': interest_rate,
#         'transactions': []
#     }

# def check_balance(state):
#     print(state['balance'])
#     return state

# def deposit(state, amount):
#     state['balance'] += amount
#     state['transactions'].append(f'Deposit of {amount}')
#     return state

# def check_withdrawl(state, amount):
#     if state['balance'] >= amount:
#         return True
#     else:
#         return False

# def withdraw(state, amount):
#     if check_withdrawl(state, amount):
#         state['balance'] -= amount
#         state['transactions'].append(f'Withdrawl of {amount}')
#     else:
#         print("Insufficient Funds!")
#     return state

# def calc_interest(state):
#     print(state['balance'] * state['interest_rate'])

# print(check_balance(withdraw(check_balance(deposit(initialize_account(), 100)), 50)))





### Functional (Advanced) ###

# class Account:
#     def __init__(self, balance=0, interest_rate=0.1, transactions=[]):
#         self.balance = balance
#         self.interest_rate = interest_rate
#         self.transactions = transactions

#     def check_balance(self):
#         print(self.balance)
#         return self

#     def deposit(self, amount):
#         self.balance += amount
#         return self

#     def check_withdrawl(self, amount):
#         if self.balance >= amount:
#             return True
#         else:
#             return False
    
#     def withdraw(self, amount):
#         if self.check_withdrawl(amount):
#             self.balance -= amount
#             return self
#         else:
#             print("Insufficient Funds!")
#             return self

#     def calc_interest(self):
#         print(self.balance * self.interest_rate)
#         return self

# atm = Account()
# atm.deposit(100).check_balance().withdraw(50).check_balance()
