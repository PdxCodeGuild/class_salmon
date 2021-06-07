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
        self.winner = 'Nobody'

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

    def calc_winner(self):
        if (self.board[0][0] == self.board[0][1]) and (self.board[0][2] == self.board[0][0]) and self.board[0][1] != ' ':
            self.winner = self.board[0][1]
            return True
        elif (self.board[1][0] == self.board[1][1]) and (self.board[1][2] == self.board[1][0]) and self.board[1][2] != ' ':
            self.winner = self.board[1][1]
            return True    
        elif (self.board[2][0] == self.board[2][1]) and (self.board[2][2] == self.board[2][0]) and self.board[2][1] != ' ':
            self.winner = self.board[2][1]
            return True
        elif (self.board[0][0] == self.board[1][0]) and (self.board[2][0] == self.board[0][0]) and self.board[1][0] != ' ':
            self.winner = self.board[2][0]
            return True
        elif (self.board[0][1] == self.board[1][1]) and (self.board[2][1] == self.board[0][1]) and self.board[2][1] != ' ':
            self.winner = self.board[1][1]
            return True
        elif (self.board[0][2] == self.board[1][2]) and (self.board[2][2] == self.board[0][2]) and self.board[1][2] != ' ':
            self.winner = self.board[2][2]        
            return True
        elif (self.board[0][0] == self.board[1][1]) and (self.board[2][2] == self.board[1][1]) and self.board[2][2] != ' ':
            self.winner = self.board[1][1]
            return True
        elif (self.board[0][2] == self.board[1][1]) and (self.board[2][0] == self.board[0][2]) and self.board[1][1] != ' ':
            self.winner = self.board[2][0]
            return True
        else:
            return False

    def is_full(self):
        for lst in b.board:
            for item in lst:
                if item == ' ':
                    return False
        else:
            return True

    def is_game_over(self):
        if b.calc_winner():    
            return True
        elif b.is_full():
            return True
        else:
            return False

player_1 = Player()
player_2 = Player()
b = Game()
print(b.__repr__())
while True:
    print(f'{player_1.player_name}\'s turn')
    b.move(player_1)  
    print(b.__repr__())
    if b.is_game_over():
        break
    print(f'{player_2.player_name}\'s turn')
    b.move(player_2)
    print(b.__repr__())
    if b.is_game_over():
        break


print('Game Over')
if b.winner == player_1.token:
    print(f'{player_1.player_name} won the game')
elif b.winner == player_2.token:
    print(f'{player_2.player_name} won the game')
else:
    print(f'{b.winner} was the winner')