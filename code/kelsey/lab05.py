# Lab 5: Pick6

# a ticket costs $2
# if 1 number matches, you win $4
# if 2 numbers match, you win $7
# if 3 numbers match, you win $100
# if 4 numbers match, you win $50,000
# if 5 numbers match, you win $1,000,000
# if 6 numbers match, you win $25,000,000
# One function you might write is pick6() which will generate a list of 6 random numbers, which can then be used for both the winning numbers and tickets. Another function could be num_matches(winning, ticket) which returns the number of matches between the winning numbers and the ticket.

# Steps
# Generate a list of 6 random numbers representing the winning tickets
import random

def pick6():
    return [random.randint(1, 99) for num in range(6)]
  
winning_ticket = pick6()
player_ticket = pick6()

def num_matches(winning_ticket, player_ticket):
    
    returns matches
if winning_ticket[1] == user_ticket[1]



# Start your balance at 0
balance = [0]

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