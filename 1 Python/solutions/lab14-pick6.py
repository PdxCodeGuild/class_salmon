"""
lab 14: pick 6 - lottery simulator
"""

import random
import time


def pick6():
    # ticket = []
    # for i in range(6):
    #     ticket.append(random.randint(1, 99))
    # return ticket
    return [random.randint(1, 99) for i in range(6)]



def calculate_payout(winning, ticket):
    """
    calculates payout based on number of matches between a ticket and the winning ticket

    :winning: list of six ints
    :ticket: list of six ints
    returns int of dollars won based on number of matches
    """
    payout = [0, 4, 7, 100, 50000, 1000000, 25000000]
    # payout = {0: 0, 1: 4, 2: 7, 3: 100, 4: 50000, 5: 1000000, 6: 25000000}
    matches = 0
    for i in range(len(ticket)):
        if winning[i] == ticket[i]:
            matches += 1

    if matches > 3:
        print(winning)
        print(ticket)
        print(f'Won ${payout[matches]}')

    return payout[matches]

    # # using comprehensions
    # matches = [winning[i] for i in range(len(winning)) if winning[i] == ticket[i]]
    # # print('matches:', matches)
    # # print('num matches:', len(matches))
    # return payout[len(matches)]


def play100k():
    # 1. Generate a list of 6 random numbers representing the winning ticket
    # 2. Start your balance at 0
    # 3. Loop 100,000 times, for each loop:
    # 4. Generate a list of 6 random numbers representing the ticket
    # 5. Subtract 2 from your balance (you bought a ticket)
    # 6. Find how many numbers match
    # 7. Add to your balance the winnings from your matches
    # 8. After the loop, print the final balance

    winning = pick6()
    balance = 0

    for i in range(100000):
        ticket = pick6()
        balance -= 2
        payout = calculate_payout(winning, ticket)
        balance += payout

    print('balance:', balance)


def main():
    start = time.time()
    for i in range(100):
        play100k()
    print(f'Finished 10,000,000 lotto calculations in {time.time() - start} seconds')


main()
