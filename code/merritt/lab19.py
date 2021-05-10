card_one = input("What is your first card? (A, 2-10, J, Q, K) ")
card_two = input("What is your second card? (A, 2-10, J, Q, K) ")
card_three = input("What is your third card? (A, 2-10, J, Q, K) ")

cards = [card_one, card_two, card_three]

counter = 0
# for card in cards:
#     if card == "A":
#         counter += 1
#     elif card in ["J", "Q", "K"]:
#         counter += 10
#     elif 2 <= int(card) <= 10:
#         counter += int(card)

card_values = {
    "A": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10
    }

for card in cards:
    if card not in card_values.keys():
        print(f"{card} is not a valid card!")
    counter += card_values.get(card) if card_values.get(card) != None else 0

    # try:
    #     counter += card_values[card]
    # except KeyError:
    #     pass

if counter < 17:
    print(f"{counter} Hit")
elif 17 <= counter < 21:
    print(f"{counter} Stay")
elif counter == 21:
    print(f"{counter} Blackjack!")
elif counter > 21:
    print(f"{counter} Already busted")