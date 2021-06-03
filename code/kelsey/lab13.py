# Lab 13: Tic-Tac-Toe
# You will write a Player class and Game class to model Tic Tac Toe, and a function main that models gameplay taking in user inputs through REPL.
class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token
        
class Game:
    def __init__(self):
        self.board = {
            (0, 0): ' ',
            (0, 1): ' ',
            (0, 2): ' ',
            (1, 0): ' ',
            (1, 1): ' ',
            (1, 2): ' ',
            (2, 0): ' ',
            (2, 1): ' ',
            (2, 2): ' '
        }

    def __repr__(self):
        return f'{self.board[(0, 0)]}|{self.board[(0, 1)]}|{self.board[(0, 2)]}|\n{self.board[(1, 0)]}|{self.board[(1, 1)]}|{self.board[(1, 2)]}|\n{self.board[(2, 0)]}|{self.board[(2, 1)]}|{self.board[(2, 2)]}|'
        
    def move(self, x, y, player):
        self.board[(x, y)] = player.token
        
    def calc_winner(self, player):
        if self.board[(0, 0)] == self.board[(0, 1)] == self.board[(0, 2)] == player.token:
            return player.token
        elif self.board[(0, 1)] == self.board[(1, 1)] == self.board[(2, 1)] == player.token:
            return player.token
        elif self.board[(0, 2)] == self.board[(1, 2)] == self.board[(2, 2)] == player.token:
            return player.token
        elif self.board[(0, 0)] == self.board[(1, 0)] == self.board[(2, 0)] == player.token:
            return player.token
        elif self.board[(1, 0)] == self.board[(1, 1)] == self.board[(1, 2)] == player.token:
            return player.token
        elif self.board[(2, 0)] == self.board[(2, 1)] == self.board[(2, 2)] == player.token:
            return player.token
        elif self.board[(0, 0)] == self.board[(1, 1)] == self.board[(2, 2)] == player.token:
            return player.token
        elif self.board[(0, 2)] == self.board[(1, 1)] == self.board[(2, 0)] == player.token:
            return player.token
        else:
            return None

#     def is_full(self):
        
#         if board == full:
#             return True

#     def is_game_over(self):
#         if game_board is full or a player has won:
#             returns True


new_game = Game()
new_player = Player('Glen', 'X')
new_game.move(0, 1, new_player)
new_game.move(0, 0, new_player)
new_game.move(0, 2, new_player)
print(new_game.calc_winner(new_player))

print(repr(new_game))

def main():
    player_1.name = input(f'Enter name of Player 1: ')
    player_2.name = input(f'Enter name of Player 2: ')

    '''
    enter both players' names
    player 1 (X) moves
    player 2 (O) moves ...
    until calc_winner == True
    '''