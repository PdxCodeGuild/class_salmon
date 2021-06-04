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

    def __repr__(self):
        fmt_out = ""
        for row in self.board:
            fmt_out += "|".join(row)
            fmt_out += "\n"
        return fmt_out

    def move(self, x, y, player_token):
        self.board[x][y] = player_token

    def calc_winner(self):
        # Check for winner in rows and columns
        # I realized doing the loop this way eliminates the counter variable and while loop...
        for each in range(3):
            row = self.board[each]
            # Check rows
            if all(square == row[0] and square != ' ' for square in row):
                return row[0]
            # check columns
            col = [self.board[square][each] for square in range(3)]
            # col = [self.board[each][square] for square in range(3)]
            if all(square == col[0] and square != ' ' for square in col):
                return col[0]
        # Check diagonal for winner
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] or self.board[0][2] == self.board[1][1] ==
            self.board[2][0]) and self.board[1][1] != ' ':
            return self.board[1][1]

        return None

    def is_full(self):
        for row in self.board:
            if any(square == ' ' for square in row):
                return False
        return True

    def is_game_over(self):
        if self.calc_winner() is None:
            return False
        elif self.calc_winner():
            return True
        elif self.is_full():
            return True
        else:
            return False
