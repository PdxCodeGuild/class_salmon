# Lab 5: Pick6

# Generate a list of 6 random numbers representing the winning tickets
import random

# One function you might write is pick6() which will generate a list of 6 random numbers, which can then be used for both the winning numbers and tickets.
def pick6():
    return [random.randint(1, 99) for i in range(6)]

# Another function could be num_matches(winning, ticket) which returns the number of matches between the winning numbers and the ticket.
def num_matches(winning_ticket, player_ticket): 
    matches = 0
    for win, tix in zip(winning_ticket, player_ticket):
        if win == tix:
            matches += 1
        return matches

winning_ticket = pick6()

# Start your balance at 0
balance = 0
counter = 0
expenses = 0
earnings = 0

# Calculate your net winnings (the sum of all expenses and earnings).
while counter <= 100000: 
    counter += 1
    expenses += 2
    player_ticket = pick6()
    if num_matches(winning_ticket, player_ticket) == 1:
        earnings += 4
    elif num_matches(winning_ticket, player_ticket) == 2:
        earnings += 7
    elif num_matches(winning_ticket, player_ticket) == 3:
        earnings += 100
    elif num_matches(winning_ticket, player_ticket) == 4:
        earnings += 50000
    elif num_matches(winning_ticket, player_ticket) == 5:
        earnings += 1000000
    elif num_matches(winning_ticket, player_ticket) == 6:
        earnings += 25000000
    balance = earnings - expenses
    print(f'Winning numbers: {winning_ticket}\nPlayer numbers: {player_ticket}')
    print(f'Number of matches: {num_matches(winning_ticket, player_ticket)}')
    print(f'Your balance: {balance}')

# Version 2
# The ROI (return on investment) is defined as (earnings - expenses)/expenses. Calculate your ROI, print it out along with your earnings and expenses.
return_on_investment = (earnings - expenses)/ expenses
print(f'Spent: {expenses}\nEarned: {earnings}\nR.O.I: {return_on_investment}')
