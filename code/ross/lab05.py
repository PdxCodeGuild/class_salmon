import random

# this function generates a ticket(list) with 6 random numbers
def pick6():
    ticket = range(6)
    ticket = [random.randint(0, 99) for nums in ticket]
    return ticket

# this function checks for the number of matches against the winning ticket numbers and returns that number
def num_matches(winning_ticket, ticket):
    matches = 0
    x = 0
    while x < 6:
        if winning_ticket[x] == ticket[x]:
            matches += 1
            x += 1
        else:
            x += 1
    return matches

#   matches = [winning_ticket[num] for num in winning_ticket if winning_ticket[num] == ticket[num]]
#   COME BACK TO THIS - WHY CAN'T I  GET THIS TO WORK?

#matches = [match + 1 for match in list1 if list1[match - 1] == list2[match - 1]]
# build function here which determines how much is won for a given number of matches
def money_won(num_matches):
    if num_matches == 0:
        return 0
    elif num_matches == 1:
        return 4
    elif num_matches == 2:
        return 7
    elif num_matches == 3:
        return 100
    elif num_matches == 4:
        return 50000
    elif num_matches == 5:
        return 1000000
    elif num_matches == 6:
        return 25000000

winning_ticket = pick6()

# player's balance starts at 0
balance = 0

# this loop runs 100,000 times and:
# generates a random ticket
# subtracts the cost of a ticket from the balance
# checks for matches between player's ticket and winnign ticket
# adds the balance from any winnings
rounds = 0
while rounds < 100000:
    rounds += 1
    balance -= 2
    ticket = pick6()
    balance += money_won(num_matches(winning_ticket, ticket)) # pass this function into another function which will determine winnigns based on matches in a given ticket

# Calculates ROI
ROI = balance / 200000

# once done looping, final balance is printed here
print(f"\nYour final balance after 100,000 rounds is ${balance}.")
print(f"That means you earned ${balance + 200000}")
print(f"And you spent $200,000.")
print(f"Your ROI was {round(ROI, 2) * 100}%.\n")