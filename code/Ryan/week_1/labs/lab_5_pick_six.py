import random

number_generator = random.randint(1, 99)

def pick_6():

    pick_6 = []

    while len(pick_6) < 7:
        pick_6.append(random.randint(1, 99))

    return pick_6

winning_numbers = pick_6()
winning_numbers.sort()
print(winning_numbers)

player_numbers = pick_6()
player_numbers.sort()
print(player_numbers)

def num_matches(winning_numbers, player_numbers):

    i = 0
    for each_number in player_numbers:

        # Does this number match the winning number at the same index?
        if each_number == winning_numbers[i]:
            output = f"Matching {each_number} at index {i}"
            continue

        i += 1

    return output