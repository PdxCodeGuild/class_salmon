#ask the user to pick three cards
card_selection1 = str(input('Pick 1 card: (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K)'))
card_selection2 = str(input('Pick 1 card: (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K)'))
card_selection3 = str(input('Pick 1 card: (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K)'))
#determine point value 
if card_selection1 == 'J' or card_selection1 == 'Q' or card_selection1 == 'K':
    card_selection1 = 10
elif card_selection1 == 'A':
    card_selection1 = 1
else:
    card_selection1 = int(card_selection1)

if card_selection2 == 'J' or card_selection2 == 'Q' or card_selection2 == 'K':
    card_selection2 = 10
elif card_selection2 == 'A':
    card_selection2 = 1
else:
    card_selection2 = int(card_selection2)

if card_selection3 == 'J' or card_selection3 == 'Q' or card_selection3 == 'K':
    card_selection3 = 10
elif card_selection3 == 'A':
    card_selection3 = 1
else:
    card_selection3 = int(card_selection3)

#Check my if statements
print(card_selection1)
print(card_selection2)
print(card_selection3)
total_pts = sum([card_selection1, card_selection2, card_selection3])
if total_pts < 17:
    print('You are advised to HIT. Your current point total is: ' + str(total_pts))
elif total_pts >= 17 and total_pts < 21:
    print('You are advised to STAY. Your current point total is: '+ str(total_pts))
elif total_pts == 21:
    print('BLACKJACK - give me your money.')
else:
    print('Already busted. Play again.')