class Player:
    def __init__(self):
        self.player_name = input('Enter player name: ')
        self.token = input('Choose "x" or "o": ')

class Game:
    def __init__(self):
        self.board = [
            [' ',' ',' '],
            [' ',' ',' '],
            [' ',' ',' ']
        ]
   

    def __repr__(self):
        output = f'''
     _ _ _
    |{self.board[0][0]}|{self.board[0][1]}|{self.board[0][2]}|
    ------- 
    |{self.board[1][0]}|{self.board[1][1]}|{self.board[1][2]}|
    ------- 
    |{self.board[2][0]}|{self.board[2][1]}|{self.board[2][2]}|
     ‾ ‾ ‾
    '''
        return output
    

    def move(self, player):
        x = int(input('Enter "x" coordinate: '))
        y = int(input('Enter "y" coordinate: '))
        self.board[x][y] = player.token   


    def calc_winner():
        while True


    # def is_full():
        


    # def is_game_over():





player_1 = Player()
b = Game()
b.move(player_1)
print(b.__repr__())