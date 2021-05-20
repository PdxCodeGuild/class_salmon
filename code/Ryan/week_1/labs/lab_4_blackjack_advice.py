"""
Lab 4: BlackJack Advice
Create a program to give basic blackjack advice.
"""

# Dictionary to give cards values
card_values = {
    "a": 1,
    "j": 10,
    "q": 10,
    "k": 10,
}


#print(card_values)

# Create a list of cards
card_inputs = []

prompt = input("Enter a card: ")
card_inputs.append(prompt)

prompt = input("Enter a second card: ")
card_inputs.append(prompt)

prompt = input("Enter a third card: ")
card_inputs.append(prompt)

#print(card_inputs)

# Calculate the total card value
total_card_value = 0

for card in card_inputs:

    # If card is a face
    if card == "j" or card == "q" or card == "k" or card == "a":
        card = card_values[card]
        #print(card)
        # Add card value to total
        total_card_value += int(card)
        continue

    else:
        #print(type(card))
        card = int(card)
        #print(card)
        #print(type(card))
        total_card_value += int(card)


if total_card_value < 17:
    print(f"{total_card_value} Hit")

elif 21 > total_card_value >= 17:
    print(f"{total_card_value} Stay")

elif total_card_value == 21:
    print(f"{total_card_value} Blackjack!")

elif total_card_value > 21:
    print(f"{total_card_value} Already Busted!")