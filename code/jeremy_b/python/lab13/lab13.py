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


if __name__ == '__main__':
    # Initialize a new game from Game class
    game = Game.Game()

    # Get human player name
    name = input('Please enter your name: ')
    # Get human player token
    try:
        token = input("Choose 'X's or 'O's:  ").upper()
        if token in ['X', 'O']:
            print(f"You have chosen {token}'s ")
        else:
            raise ValueError
    except ValueError:
        print("Please enter 'X' or 'O'!")

    player1 = Player.Player(name, token)
    player2 = Player.Player("Computer", create_computer_token(token))

    print(f"{player1.name} is {player1.token}\n{player2.name} is {player2.token}")

    turn_counter = 1
    available_squares = ['0,0', '0,1', '0,2', '1,0', '1,1', '1,2', '2,0', '2,1', '2,2']
    while not game.is_game_over():
        # find current player
        current_player = player1 if turn_counter % 2 != 0 else player2
        # Take turn
        if current_player == player1:
            print(game)
            try:
                choice = input("Please enter a square: ")
                if choice in available_squares:
                    available_squares.pop(available_squares.index(choice))
                else:
                    raise ValueError
            except ValueError:
                print("Invalid square choice or square not available.")
            choice = choice.split(",")
            choice = [int(num) for num in choice]
            game.move(choice[0], choice[1], current_player.token)
            turn_counter += 1
        else:
            # Computer player goes
            # computer player chooses an available square
            choice = available_squares[random.randint(0, len(available_squares) - 1)]
            available_squares.pop(available_squares.index(choice))
            choice = choice.split(",")
            choice = [int(num) for num in choice]
            game.move(choice[0], choice[1], current_player.token)
            turn_counter += 1

    if not game.is_full():
        print(game)
        print(f"Winner: {game.calc_winner()}")
    else:
        print(game)
        print(f"It's a tie!")



