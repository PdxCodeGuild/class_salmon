import random

winning_ticket = []

ticket = []

expenses = 0

income = 0

matches = 0

win_values = {
0: 0,
1: 4,
2: 7,
3: 100,
4: 50000,
5: 1000000,
6: 25000000,
}

def win_value(x):
    return win_values[x]



def validate(x):
    global matches
    # print(x)
    for i, value in enumerate(x):
        if winning_ticket[i] == value:
            matches += 1
    return matches


def winning_nums():
    for i in range(6):
        x = random.randint(1, 99)
        winning_ticket.append(x)
    return winning_ticket


def buy_ticket():
    global expenses
    expenses += 2
    for i in range(6):
        x = random.randint(1, 99)
        ticket.append(x)
    return ticket


winning_ticket = winning_nums()

for i in range(100000):
    ticket = buy_ticket()
    x = validate(ticket)
    income += win_value(x)
    ticket = []
    matches = 0


print(f'You spent ${expenses} and gained ${income}.')

