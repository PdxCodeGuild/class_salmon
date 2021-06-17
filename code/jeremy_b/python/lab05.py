"""

Author: Jeremy Bush
Project: Programming Boot Camp Lab 05
Version: 1
Date: 5/20/2021

"""
import random


# Generate a list of 6 random numbers for ticket.  Can be used for winning and user tickets.
def generate_ticket():
    ticket = random.sample(range(1, 99), 6)
    return ticket


# Compare the winning numbers to the user's numbers
def compare_tickets(winning_ticket, user_ticket):
    user_winnings = []
    for number in winning_ticket:
        if winning_ticket[winning_ticket.index(number)] == user_ticket[winning_ticket.index(number)]:
            user_winnings.append(number)
    return user_winnings

# Calcualte the winnings earned
def winning_values(winnings):
    if len(winnings) == 1:
        return 4
    elif len(winnings) == 2:
        return 7
    elif len(winnings) == 3:
        return 100
    elif len(winnings) == 4:
        return 50000
    elif len(winnings) == 5:
        return 1000000
    elif len(winnings) == 6:
        return 25000000


# variables to hold balance and winnings
balance = 0
winnings = 0

# Get winning numbers
winning_numbers = generate_ticket()

# loop for simulating 100,000 plays.
counter = 1
while counter <= 100000:

    # generate user ticket
    user_ticket = generate_ticket()

    print(f"Evaluating ticket #{counter}. Your numbers: {user_ticket}")

    # deduct 2 from user balance
    balance -= 2

    # list of user's winning numbers:
    user_winnings = compare_tickets(winning_numbers, user_ticket)

    # Check for wins and add any value to winnings
    if len(user_winnings) != 0:
        winnings += winning_values(user_winnings)
        counter += 1
    else:
        counter += 1

# print the total winnings and total spent.
print(f"\nThe winning numbers were: {winning_numbers}")

if balance < winnings:
    print("Unfortunately, you spent $" + "{:,}".format(abs(balance)) + ", but only won $" + "{:,}".format(winnings) + ".")
    print("Your final balance is $" + "{:,}".format(winnings + balance) + ".")
else:
    print(f"Congratulations! You won ${winnings} and only spent $'{abs(balance)}!")
    print("Congratulations! You won $" + "{:,}".format(winnings) + " and only spent $" + "{:,}".format(abs(balance))) + "!"
    print("Your final balance is $" + "{:,}".format(winnings + balance) + ".")
