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

rules = {0: (0-2),
         1: (4-2),
         2: (7-2),
         3: (100-2),
         4: (50000-2),
         5: (1000000-2),
         6: (25000000-2)}


current_matches = 0
how_many = int(input('How many tickets do you want to buy?  '))
balance = 0
count_loops = 0

while True:
    if count_loops == (how_many):
        break
    else:
        current_matches = (num_matches(winners, ticket))
        count_loops += 1
        balance += rules[current_matches]


if balance < 0:
    print(
        f'You bought {how_many} tickets and LOST ${abs(balance)}! \nYou should have used that money to invest in Dogecoin!')
else:
    print(
        f'You bought {how_many} tickets and won ${balance}!! \nNow go invest your winnings in Dogecoin.')
