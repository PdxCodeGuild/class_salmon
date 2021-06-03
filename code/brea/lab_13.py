class player:
def __init__(self, x, y):
    self.player_name = input('Enter your player name: ')
    self.token = input('Choose "x" or "o": ')

class Board:
    def __init__(self):
        self.board = [[ , , ],
    [ , , ],
    [  , , ]]

    def __repr__(self):
        board_rep = ''
        for i in board:
            for j in i:
                board_rep += j
        print(board_rep)
    
    def move(self, x, y, player):
        self.move = input('Enter your coordinates: ')


