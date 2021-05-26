import random
import secrets

def pick6():
    # return [random.randint(1, 99) for x in range(6)]
    return [secrets.randbelow(99) + 1 for x in range(6)]
    # ticket = []
    # for x in range(6):
    #     ticket.append(random.randint(1,99))
    # return ticket

def num_matches(winning, ticket):
    matches = 0
    # for i in range(len(winning)):
    #     if winning[i] == ticket[i]:
    #         matches +=1
    for win, tix in zip(winning, ticket):
        if win == tix:
            matches += 1
    return matches

# def num_matches(winning, ticket):
#     matches = 0
#     for num in ticket:
#         if num in winning:
#             matches += 1
#     return matches

winnings = {6: 25000000, 5: 1000000, 4: 50000, 3: 100, 2: 7, 1: 4, 0: 0}

num_of_matches = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

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

print("balance:", balance)
print("expenses:", expenses)
print("earnings", earnings)
print("roi:",(earnings - expenses)/expenses)
print(num_of_matches)
