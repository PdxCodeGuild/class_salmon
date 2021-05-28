#game of tic tac toe Lab13
class Player:
    def __init__(self, name = 'hey you', token = 'b'):#when the args have something assigned these are defaults
        self.name = name
        self.token = token
board = [('','',''),('','',''),('','','')]      
class Game:
    def __repr__(self, board):
        self.board = board
        return print(board)
print(Game.__repr__)#printing the memory location