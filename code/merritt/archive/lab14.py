import random

def pick6():
    return [random.randint(1,99) for x in range(6)]
    # ticket = []
    # for x in range(6):
    #     ticket.append(random.randint(1,99))
    # return ticket

def num_matches(winning, ticket):
    matches = 0
    # for i in range(len(winning)):
    #     if winning[i] == ticket[i]:
    #         matches += 1
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

winnings = {6: 25000000, 5: 1000000, 4: 50000, 3: 100, 2: 0, 1: 0, 0: 0}

balance = 0
earnings = 0
expenses = 0

num_of_matches = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

winning_ticket = pick6()

for n in range(1000000):
    current_ticket = pick6()
    balance -= 2
    expenses += 2
    matches = num_matches(winning_ticket, current_ticket)
    balance += winnings[matches]
    earnings += winnings[matches]
    num_of_matches[matches] += 1
    # if matches == 6:
    #     balance += 25000000
    #     earnings += 25000000
    #     m6 += 1
    # elif matches == 5:
    #     balance += 1000000
    #     earnings += 1000000
    #     m5 += 1
    # elif matches == 4:
    #     balance += 50000
    #     earnings += 50000
    #     m4 += 1
    # elif matches == 3:
    #     balance += 100
    #     earnings += 100
    #     m3 += 1
    # elif matches == 2:
    #     balance += 7
    #     earnings += 7
    #     m2 += 1
    # elif matches == 1:
    #     balance += 4
    #     earnings += 4
    #     m1 += 1
    # else:
    #     m0 += 1

print("balance:", balance)
print("expenses:", expenses)
print("earnings:", earnings)
print("roi:", (earnings - expenses)/expenses)
print(num_of_matches)