class ATM:
    def __init__(self, balance=0):
        self.__balance = balance
        self.__transactions = []

    def check_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount
        self.__transactions.append(f"Deposit of ${amount}: New balance ${self.__balance}")

    def __check_withdrawl(self, amount):
        # if self.balance >= amount:
        #     return True
        # return False
        
        # return True if self.balance >= amount else False

        return self.__balance >= amount

    def withdrawl(self, amount):
        if self.__check_withdrawl(amount):
            self.__balance -= amount
            self.__transactions.append(f"Withdrawl of ${amount}: New balance ${self.__balance}")
        else:
            # print("not enough money!")
            raise ValueError("Not enough money in account to process transaction!")

    def print_transactions(self):
        print("\n".join(self.__transactions))

account = ATM()

while True:
    print("What would you like to do ([d]eposit, [w]ithdraw, [c]heck balance, [h]istory, [q]uit)?")
    user_input = input()

    if user_input in ["deposit", "d"]:
        print("How much would you like to deposit?")
        user_amount = input()
        account.deposit(float(user_amount))
        # account.deposit(float(input("How much?")))
    elif user_input in ["withdrawl", "w"]:
        print("How much would you like to withdrawl?")
        user_amount = input()
        try:
            account.withdrawl(float(user_amount))
        except ValueError as e:
            print(e)
    elif user_input in ["check balance", "check", "balance", "c"]:
        print(f"Your account balance is: ${account.check_balance()}")
    elif user_input in ["history", "h"]:
        account.print_transactions()
    elif user_input in ["quit", "exit", "q"]:
        break
    else:
        print("I'm sorry, I didn't understand that. Please try again.")

