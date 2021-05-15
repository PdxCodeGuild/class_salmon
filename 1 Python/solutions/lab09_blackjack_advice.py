
cards = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
         '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10,  'K': 10}


card1 = input('What is your first card?')
card2 = input('what is your second card?')
card3 = input('what is your third card?')

card1_value = cards[card1]
card2_value = cards[card2]
card3_value = cards[card3]

total = card1_value + card2_value + card3_value

print('Hand total:', total)

if total < 17:
    print('Hit')
elif total >= 17 and total < 21:
    print('Stay')
elif total == 21:
    print('Blackjack!')
else:
    print('Busted!')
