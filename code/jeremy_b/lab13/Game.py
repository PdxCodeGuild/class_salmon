"""

Author: Jeremy Bush
Project: Programming Boot Camp Lab 13, Game Class
Version: 1
Date: 06/02/2021

"""
import random


class Game:
    def __init__(self):
        self.board = [[' ' for row in range(3)] for each in range(3)]
        self.available_squares = ['0,0', '0,1', '0,2', '1,0', '1,1', '1,2', '2,0', '2,1', '2,2']

    def __repr__(self):
        fmt_out = ""
        for row in self.board:
            fmt_out += "|".join(row)
            fmt_out += "\n"
        return fmt_out

    def move(self, x, y, player_token):
        self.board[x][y] = player_token

    def calc_winner(self):
        # check for winner in row
        for row in self.board:
            if all(square == row[0] and square != ' ' for square in row):
                return row[0]
        # Check for winner in column
        counter = 0
        while counter < len(self.board):
            if (self.board[0][counter] == self.board[1][counter] == self.board[2][counter]) and self.board[0][counter] != ' ':
                return self.board[0][counter]
            else:
                counter += 1
        # Check for winner in diagonal
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] or self.board[0][2] == self.board[1][1] ==
            self.board[2][0]) and self.board[1][1] != ' ':
            return self.board[1][1]

        return None

    def is_full(self):
        for row in self.board:
            for square in row:
                if any(square) == ' ':
                    return False
                else:
                    return True

    def is_game_over(self):
        if self.calc_winner() is None:
            return False
        elif 
            return True
        elif self.is_full():
            return True
        else:
            return False

    def play(self, player1, player2, player1_token, player2_token):
        turn_counter = 1
        print(" Tic Tac Toe ".center(26, "="))
        while turn_counter <= 9:
            print(self.__repr__())
            # determine player's turn:
            # Human player goes first
            if turn_counter % 2 != 0:
                print(f"{player1}, it's your turn...")
                try:
                    choice = input("Enter point to place your token: ")
                    if choice in self.available_squares:
                        # remove this choice from the list of available points
                        self.available_squares.pop(self.available_squares.index(choice))
                        # Convert the choice to list of ints:
                        choice = choice.split(',')
                        # Make the players move
                        self.move(int(choice[0]), int(choice[1]), player1_token)
                        turn_counter += 1
                    else:
                        raise ValueError
                except ValueError:
                    print("You chose an invalid square.  Please try again...")

            else:
                # Computer takes a turn:
                print(f"{player2} is taking their turn...")
                choice = self.available_squares[random.randint(0, len(self.available_squares) - 1)]
                print(f"Computer chooses square {choice}.")
                self.available_squares.pop(self.available_squares.index(choice))
                choice = choice.split(',')
                self.move(int(choice[0]), int(choice[1]), player2_token)
                turn_counter += 1

