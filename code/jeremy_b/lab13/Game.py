"""

Author: Jeremy Bush
Project: Programming Boot Camp Lab 13, Game Class
Version: 1
Date: 06/02/2021

"""


class Game:
    def __init__(self):
        self.board = [
            ["0,0", "0,1", "0,2"],  # Line 1
            ["1,0", "1,1", "1,2"],  # Line 2
            ["2,0", "2,1", "2,2"]   # Line 3
        ]
        self.turns = []

    def move(self, x, y, player_token):
        self.board[x][y] = player_token

    def __repr__(self):
        for square in self.board:
            print(f'{square[0]} | {square[1]} | {square[2]}')

    def calc_winner(self):
        pass

    def is_full(self):
        counter = 0
        for square in self.board:
            for point in square:
                if point != ' ':
                    counter += 1
        if counter == 9:
            return True
        else:
            return False

    def is_game_over(self):
        if self.calc_winner():
            return True
        else:
            return False

    def game_turns(self, players):
        while len(self.turns) < 9:
            if len(self.turns) % 2 == 0:
                self.turns.append(players[0])
            else:
                self.turns.append(players[1])

    def play_game(self):
        print(self.board)
