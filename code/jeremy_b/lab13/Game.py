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
        # check for winner in row
        for row in self.board:
            if all(square == row[0] and square != ' ' for square in row):
                return f"Winner is {row[0]}'s!"
        # Check for winner in column
        counter = 0
        while counter < len(self.board):
            if (self.board[0][counter] == self.board[1][counter] == self.board[2][counter]) and self.board[0][counter] != ' ':
                return f"Winner is {self.board[0][counter]}'s"
        # Check for winner in diagonal
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] or self.board[0][2] == self.board[1][1] == self.board[2][0]) and self.board[1][1] != ' ':
            return f"Winner is {self.board[1][1]}'s!"    

    def is_full(self):
        for row in self.board:
            for square in row:
                if square == ' ':
                    return False
                else:
                    return True

    def is_game_over(self):
        if not self.calc_winner():
            return False
        elif not self.is_full():
            return False
        else:
            return True


