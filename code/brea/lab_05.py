import random

balance = 0

match1 = 4
match2 = 7
match3 = 100
match4 = 50000
match5 = 1000000
match6 = 25000000


def create_ticket():
    ticket = []
    for x in range(6):
        x = (random.randint(0,99))
        ticket.append(x)
    return ticket    

def compare_tickets(winning_ticket, your_ticket):
    number_matches = 0
    for item,value in enumerate(your_ticket):
        print(winning_ticket[item],value) 
        if winning_ticket[item] == value:
            number_matches += 1
    return number_matches

def pick_ticket():
    ticket = []
    for x in range(6):
        num = random.randint(0,99)
        ticket.append(int(num))
    return ticket    

chosen_ticket = pick_ticket()
print(chosen_ticket)

test_ticket = create_ticket()
print(test_ticket)

winning_ticket = create_ticket()
x = compare_tickets(test_ticket,winning_ticket)
print(x)

def money_balance():
         balance += (-2)
    if matches 



# print(output)