import random

cost = 0
winnings = 0

winnings_dict = { 0: 0,
1: 4,
2: 7,
3: 100,
4: 50000,
5: 1000000,
6: 25000000,
}

number_matches = 0
ticket = []


def create_ticket():
    global ticket
    ticket = []
    for x in range(6):
        x = (random.randint(0,99))
        ticket.append(x)
    return ticket    

def compare_tickets(winning_ticket, your_ticket):
    global number_matches
    number_matches = 0
    for index, value in enumerate(your_ticket):
        # print(winning_ticket[index],value) 
        if winning_ticket[index] == value:
            number_matches += 1
    return number_matches 

for x in range(100000):
    cost = cost+2
    win_ticket = create_ticket()
    your_ticket = create_ticket()
    number_matches = compare_tickets(win_ticket,your_ticket)
    win_value = winnings_dict[number_matches]
    winnings += win_value
roi = (winnings - cost) / cost

output = f'You won {winnings}, and you spent {cost}, your investment return value was {roi}'
print(output)