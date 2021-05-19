# Get users card picks
print("Hello! Please choose three cards.")
first_card = input("\nPick your first card (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K): ").upper()
second_card = input("\nPick your second card (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K): ").upper()
third_card = input("\nPick your third card (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K): ").upper()

# add a dictionary to correlate card with their values
values = {
    'A': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
}

# sum the user's input
total_value = [values[first_card], values[second_card], values[third_card]]
total_value = sum(total_value)

# this function determines the advice to give user
def advice():
    if total_value < 17:
        return "Hit"
    elif total_value >= 17 and total_value < 21:
        return "Stay"
    elif total_value == 21:
        return "Blackjack!"
    elif total_value > 21:
        return "Already Busted"

print("\n", total_value, advice(), "\n")