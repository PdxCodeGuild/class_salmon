card_1 = input('First card: ')
card_2 = input('Second card: ')
card_3 = input('Third card: ')

card_value = {'A' : 1,
'2' : 2,
'3' : 3,
'4' : 4,
'5' : 5,
'6' : 6,
'7' : 7,
'8' : 8,
'9' : 9,
'J' : 10,
'Q' : 10,
'K' : 10
}

hand = (card_1 + card_2 + card_3)

if hand < 17:
    output = 'Hit'
elif hand >= 17 but > 21:
    output = 'Stay'    
elif hand = 21:
    output = 'Blackjack!'
else: 
    output = 'Bust'    

print(output)