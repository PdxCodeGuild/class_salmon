#first computer picks 6 random numbers as winner
#second try picking 6 100,000 times
import random
import secrets #different style random generator
#secret pick6
'''def pick6_secret():
    return[secrets.randbelow(99) + 1 for x in range(6)]'''
#returns a random thing, no parameters
'''def pick6():
    ticket = []
    for i in range(6):
        ticket.append(random.randint(1, 99))
    return ticket
#when you print something you are putting it on the command line in the terminal
print(pick6())'''
def pick6():
    return [random.randint(1,99) for x in range(6)]
#do a number of matches function
'''def num_matches(winning, ticket):
    matches = 0 
    #does not matter if you do length of winning or ticket
    for i in range(len(winning)):
        if winning[i] == ticket[i]:
            matches += 1
    for win, tix in zip(winning, ticket):
        if win == tix:
            matches += 1
        #if it does not match then the function does not do anything
    return matches'''
#this game below looks for any number, in any order, rather than in order
def num_matches(winning, ticket):
    matches = 0
    for num in ticket:
        if num in winning:
            matches += 1
    return matches
#the above can also be done with a zip
#there are different ways to do this. 
#create empty list, iterate through it, or do a list comprehension
winnings = {6: 25000000, 5:1000000, 4:50000, 3:100, 2:7, 1:4, 0:0}
num_of_matches = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0} #not a requirement of the lab but has good functionality add
winning_ticket = pick6()

balance = 0
earnings = 0
expenses = 0

for n in range(100000):
    current_ticket = pick6()
    balance -= 2
    expenses += 2
    matches = num_matches(winning_ticket, current_ticket)
    balance += winnings[matches]
    earnings += winnings[matches]
    num_of_matches[matches] += 1

print("balance: ", balance)
print("expenses: ", expenses)
print("earnings: ", earnings)
print("roi: ",(earnings - expenses)/expenses)
print("number of matches: ", num_of_matches)
'''def pick6():
    return [random.random.randint(1,99) for x in range(6)]'''
#the above is a list comprehension
#zip is going to pack each list into tuples


