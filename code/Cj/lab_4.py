import random

menu_nav =''

user_error = "Error! Please make a valid entry: "

rules = '''

Basic Blackjack Rules:

The goal of blackjack is to beat the dealer's hand without going over 21.
Face cards are worth 10. Aces are worth 1 or 11, whichever makes a better hand.
Each player starts with two cards, one of the dealer's cards is hidden until the end.
To 'Hit' is to ask for another card. To 'Stand' is to hold your total and end your turn.
If you go over 21 you bust, and the dealer wins regardless of the dealer's hand.
If you are dealt 21 from the start (Ace & 10), you got a blackjack.
Blackjack usually means you win 1.5 the amount of your bet. Depends on the casino.
Dealer will hit until his/her cards total 17 or higher
 
Source: http://www.hitorstand.net/strategy.php
'''


main_menu = '''

    Welcome to Blackjack!.

    1. Play!

    2. View rules.

    3. Exit.

    Enter: '''

return_menu = '''
    1. Back to Main Menu

    2. Quit
        
    Enter: '''


while True:

    UI = int(input(f'{main_menu}'))
    
    if UI == 1 or UI == 3:
        break
    if UI == 2:
        print(rules)
        while menu_nav != 1 or menu_nav != 2:
            if menu_nav == '':
                menu_nav = input(f'{return_menu}')
            elif menu_nav == 1:
                break

            else:
                menu_nav = input(f'{return_menu.replace("Enter: ", user_error)}')
      
        
    else: 
        main_menu = main_menu.replace("Enter: ", user_error)


        

