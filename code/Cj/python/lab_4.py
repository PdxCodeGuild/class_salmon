import random

card_values = {
    'A': 1,
    'J': 0,
    'Q': 0,
    'K': 0,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    
}
























































# user_error = "Error! Please make a valid entry: "

# rules = '''

# Basic Blackjack Rules:

# The goal of blackjack is to beat the dealer's hand without going over 21.
# Face cards are worth 10. Aces are worth 1 or 11, whichever makes a better hand.
# Each player starts with two cards, one of the dealer's cards is hidden until the end.
# To 'Hit' is to ask for another card. To 'Stand' is to hold your total and end your turn.
# If you go over 21 you bust, and the dealer wins regardless of the dealer's hand.
# If you are dealt 21 from the start (Ace & 10), you got a blackjack.
# Blackjack usually means you win 1.5 the amount of your bet. Depends on the casino.
# Dealer will hit until his/her cards total 17 or higher
 
# Source: http://www.hitorstand.net/strategy.php
# '''


# main_menu = '''

#     Welcome to Blackjack!.

#     1. Play!

#     2. View rules.

#     3. Exit.

#     Enter: '''

# return_menu = '''
#     1. Back to Main Menu

#     2. Quit
        
#     Enter: '''


# while True: ### Menu navigtion system
#     menu_nav = input(f'{main_menu}')
#     try:
#         if menu_nav.isnumeric():
#             menu_nav = int(menu_nav)
#             if menu_nav == 3: ###### Exit game
#                 exit()
#             elif menu_nav == 2: #### Print rules and enter retuen menu loop
#                 print(rules)
#                 # menu_nav = '' # Reseting navigation value to entey condition of next loop
#                 while menu_nav.isnumeric():
#                     menu_nav = (input(f'{return_menu}'))
#                     try:
#                         if menu_nav.isnumeric():
#                             menu_nav =int(menu_nav)
#                             try:
#                                 if menu_nav == 1:
#                                     break


#                                                 while menu_nav != '':
#                                                     try:
#                                                         if menu_nav.isnumeric():
#                                                             menu_nav = int(menu_nav)
                                                        
#                                                             try:
#                                                                 if menu_nav.isnumeric() and int(menu_nav) == 1 or int(menu_nav) == 2:
#                                                                     menu_nav = int(menu_nav)
#                                                                     if menu_nav ==1:
#                                                                         break
#                                                                     else:
#                                                                         exit()
#                                                                 else:
#                                                                     raise ValueError('Incorrect input ')
#                                                             except ValueError:
#                                                                 menu_nav = input(f'{return_menu.replace("Enter: ", user_error)}')
#                                                         else:
#                                                             raise ValueError('Incorrect input ')
#                                                     except ValueError:
#                                                         menu_nav = input(f'{return_menu.replace("Enter: ", user_error)}')
                                                       
                                                        
#                         else:
#                             raise ValueError
#                     except ValueError:
#                         return_menu = return_menu.replace("Enter: ", user_error)

#             # elif menu_nav == 1: ############# Start of Game


#             else: 
#                 main_menu = main_menu.replace("Enter: ", user_error)
#         else:
#             raise ValueError('Incorrect input ')   
#     except ValueError:
#         main_menu = main_menu.replace("Enter: ", user_error)