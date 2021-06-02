"""

Author: Jeremy Bush
Project: Programming Boot Camp Lab 13, Main section
Version: 1
Date: 06/02/2021

"""


import Game
import Player
import random


def create_computer_token(player_token):
    # Setup computer player
    if player_token.upper() == 'X':
        return 'O'
    else:
        return 'X'


# Initialize a new game from Game class
game = Game.Game()

# Get human player name
name = input('Please enter your name: ')
# Get human player token
try:
    token = input("Choose 'X's or 'O's:  ")
    if token.upper() in ['X', 'O']:
        print(f"You have chosen {token}'s ")
    else:
        raise ValueError
except ValueError:
    print("Please enter 'X' or 'O'!")

player1 = Player.Player(name, token)
player2 = Player.Player("Computer", create_computer_token(token))

print(f"{player1.name} is {player1.token}\n{player2.name} is {player2.token}")




