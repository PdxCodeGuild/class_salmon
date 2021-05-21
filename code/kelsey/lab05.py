# Lab 5: Pick6

# Generate a list of 6 random numbers representing the winning tickets
import random

# One function you might write is pick6() which will generate a list of 6 random numbers, which can then be used for both the winning numbers and tickets.
def pick6():
    return [random.randint(1, 99) for i in range(6)]
  
winning_ticket = pick6()
player_ticket = pick6()

# Another function could be num_matches(winning, ticket) which returns the number of matches between the winning numbers and the ticket.
def num_matches(winning_ticket, player_ticket): # just returning numbers of matches
    number_of_matches = 0
    number_of_matches += 1
    if winning_ticket[i] == player_ticket[i]: # if statement inside of a loop
        return number_of_matches

# Start your balance at 0
balance = 0
# a ticket costs $2
balance -= 2


if num_matches == 1:
    balance += 4
elif num_matches ==2:
    balance += 7
elif num_matches == 3:
    balance += 100
elif num_matches == 4:
    balance += 50000
elif num_matches == 5:
    balance += 1000000
elif num_matches == 6:
    balance += 25000000


# Loop 100,000 times, for each loop:
# Generate a list of 6 random numbers representing the ticket
# Subtract 2 from your balance (you bought a ticket)
# Find how many numbers match
# Add to your balance the winnings from your matches
# After the loop, print the final balance

# Version 2
# The ROI (return on investment) is defined as (earnings - expenses)/expenses. Calculate your ROI, print it out along with your earnings and expenses.
# return_on_investment = (earnings - expenses)/expenses
# print(return_on_investment)