first_card = input('What\'s your first card, playa?  ')
second_card = input('What\'s your second card, playa?  ')
third_card = input('What\'s your third card, playa?  ')

card_val = {'A': 1,
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
            'K': 10
            }
sum_cards = (card_val[first_card] +
             card_val[second_card] + card_val[third_card])

if sum_cards < 17:
    advice = "You should hit."
elif sum_cards >= 17 and sum_cards < 21:
    advice = "You should stay."
elif sum_cards == 21:
    advice = "BLACKJACK, BABY!!!"
elif sum_cards > 21:
    advice = "Daww... BUST!"

print(f'You\'ve got {sum_cards}. \n{advice}')
