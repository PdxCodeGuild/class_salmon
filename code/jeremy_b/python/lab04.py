"""

Author: Jeremy Bush
Project: Programming Boot Camp Lab 04
Version: 1
Date: 5/19/2021

"""


# Define function for calculating card total
def card_total(cards):
    # define dictionary for face card values.
    card_values = {
        "A": 1,
        "J": 10,
        "Q": 10,
        "K": 10
    }

    # SPlit the string into a list.
    cards = cards.split(",")

    # Check cards to see if any face cards included.  If there are, replace the face card with appropriate value
    for card in cards:
        if card in ["A", "J", "Q", "K"]:
            cards[cards.index(card)] = int(card_values[card])
        else:
            cards[cards.index(card)] = int(card)

    # get value and return total.
    card_total_value = 0
    for card in cards:
        card_total_value += card

    if card_total_value < 17:
        return "You should hit!"
    elif 17 <= card_total_value < 21:
        return "You should stay!"
    elif card_total_value == 21 and len(cards) == 2:
        return "Blackjack!"
    elif card_total_value == 21 and len(cards) > 2:
        return "You win with 21!"
    else:
        return "You bust!"


# Have user input their cards
print("Please enter your hand from the following cards.  Separate each card with a comma:")
print("A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K\n")
user_hand = input("Enter your hand: ")

# Check for and eliminate spaces.
user_hand = user_hand.replace(" ", "")
# Print result to screen.
print(card_total(user_hand))
