import random

winning_ticket = []

ticket = []

balance = 0

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
    global balance
    balance -= 2
    expenses += 2
    for i in range(6):
        x = random.randint(1, 99)
        ticket.append(x)
    return ticket


# def get_percentage(x, y):
#     return f'{(x / y) * 100}%'




winning_ticket = winning_nums()

for i in range(100000):
    ticket = buy_ticket()
    validation = validate(ticket)
    income += win_value(validation)
    ticket = []
    matches = 0

# loss = abs(income - expenses)
# loss_percent = get_percentage(loss, expenses)
roi = (income - expenses) / expenses
# print(loss_percent)
output = (f'You spent ${expenses} and gained ${income}. And your return on investment was {roi}')
print(output)

