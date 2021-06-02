"""

Author: Jeremy Bush
Project: Programming Boot Camp Lab 13, Game Class
Version: 1
Date: 06/02/2021

"""


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
        if self.board[x][y] != ' ':
            return "Space already taken."
        else:
            self.board[x][y] = player_token

    def calc_winner(self):
        pass

    def is_full(self):
        for row in self.board:
            for square in row:
                if square == ' ':
                    return False
                else:
                    return True

    def is_game_over(self):
        if not self.calc_winner():
            return True
        elif self.is_full():
            return False
        else:
            return False


