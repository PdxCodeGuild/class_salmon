# program will break if user inputs any value outside of the dictionary

playing_cards = {
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

# asking the user for their first card
first_card = input("\nWhat's your first card? ")
# asking the user for their second card
second_card = input("\nWhat's your second card? ")
# asking the user for their third card
third_card = input("\nWhat's your third card? ")

# finds the value of their first card from the dictionary
first = playing_cards[first_card]
# finds the value of their second card from the dictionary
second = playing_cards[second_card]
# finds the value of their third card from the dictionary
third = playing_cards[third_card]

# combines the total of the three cards
hand_total = first + second + third

# if total is a blackjack
if hand_total == 21:
    print(f"\n{hand_total} is blackjack!")
# if total is between 17 and 20 will advise the user to stay
elif hand_total >= 17 and hand_total <= 20:
    print(f"\n{hand_total} stay.")
# if total is below 17 will advice the user to hit
elif hand_total <= 16:
    print(f"\n{hand_total} hit.")
# everything else would be above 21 and it is a bust
else: 
    print(f"\n{hand_total} bust!")