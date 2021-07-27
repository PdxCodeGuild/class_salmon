import random


def pick6():
    temporay = []
    for i in range(6):
        temporay.append(random.randint(1, 99))
    return temporay


ticket = pick6()
winners = pick6()

#ticket = [0, 1, 2, 3, 5, 6]
#winners = [1, 2, 3, 4, 5, 6]


def num_matches(winners, ticket):
    count_matches = 0
    current_idx = 0
    while current_idx <= 5:
        for num in winners:
            if winners[current_idx] == ticket[current_idx]:
                count_matches += 1
                current_idx += 1
                ticket = pick6()

            else:
                current_idx += 1
                ticket = pick6()
    return count_matches


# print(num_matches(winners, ticket))

rules = {0: (0),
         1: (4),
         2: (7),
         3: (100),
         4: (50000),
         5: (1000000),
         6: (25000000)}


current_matches = 0
how_many = int(input('How many tickets do you want to buy?  '))
winnings = 0
count_loops = 0
expenses = how_many * 2
while True:
    if count_loops == (how_many):
        break
    else:
        current_matches = (num_matches(winners, ticket))
        count_loops += 1
        winnings += rules[current_matches]

balance = winnings - expenses

if balance < 0:
    print(
        f'You bought {how_many} tickets and are now ${abs(balance)} poorer! \nYou should have used that money to invest in Dogecoin!')
else:
    print(
        f'You bought {how_many} tickets and won ${balance}!! \nNow go invest your winnings in Dogecoin.')


print(
    f'Your earnings are: ${winnings}  \nYour expenses are: ${expenses} \nYour ROI is {(winnings - expenses) / expenses}')
