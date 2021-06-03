class Player:
    def __init__(self,player,token):
        self.player = player
        print(player)
        self.token = token
        print(token)
class Game:
    def __init__(self):
        self.board = {1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
    def __repr__(self):
        self.board_string = f'\n{self.board[1]}|{self.board[2]}|{self.board[3]}\n{self.board[4]}|{self.board[5]}|{self.board[6]}\n{self.board[7]}|{self.board[8]}|{self.board[9]}\n'
        return self.board_string
    def move(self,number,player):
        if self.board[number] == ' ':
            self.board[number] = player.token
        else:
            return 'Space taken'
    '''def calc_winner(self):
        if self.board[5] == player.token:
            if self.board[1] == player.token:
                if self.board[9] == player.token:
                    return player.token
            elif self.board[7] == player.token:
                if self.board[3] == player.token:
                    return player.token
            elif self.board[2] == player.token:
                if self.board[8] == player.token:
                    return player.token
            elif self.board[4] == player.token:
                if self.board[6] == player.token:
                    return player.token
        elif self.board[1] ==player.token:
            if self.board[2] == player.token:
                if self.board[3] == player.token:
                    return player.token
            elif self.board[4] == player.token:
                if self.board[7] == player.token:
                    return player.token
        elif self.board[9] ==player.token:
            if self.board[8] == player.token:
                if self.board[7] == player.token:
                    return player.token
            elif self.board[6] == player.token:
                if self.board[3] == player.token:
                    return player.token
        else:
            return None
    def is_full(self):
        for i,xo in (self.board).items():
            if xo ==' ':
                return False
        return True
    def is_game_over(self):
        if self.calc_winner() == Player.token:
            return True
        elif self.is_full():
            return True'''
#game = Game()
#player1 = Player(1,'O')
#player2 = Player(2,'X')
#player2 = Player('player 2', 'O')
def main():
    game = Game()
    player1 = Player(1,'O')
    player2 = Player(2,'X')
    print("Welcome to tic-tac_toe. Players take turns placing tokens (a 'O' or 'X') into a 3x3 grid. Whoever gets three in a row first wins.")
    #while game.is_game_over() != True:
    print(Game.__repr__)
print(main())
        
