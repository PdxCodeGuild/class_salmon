class Player:
    def __init__(self,player,token):
        self.player = player
        self.token = token
class Game:
    def __init__(self):
        self.board = {1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
    def __repr__(self):
        self.board_string = f'\n game\t\t key\n{self.board[1]}|{self.board[2]}|{self.board[3]}\t\t1|2|3\n{self.board[4]}|{self.board[5]}|{self.board[6]}\t\t4|5|6\n{self.board[7]}|{self.board[8]}|{self.board[9]}\t\t7|8|9\n'
        return self.board_string
    def move(self,number,player):
        self.board[int(number)] = player.token
    def calc_winner(self, player):
        if self.board[5] == player.token:
            if self.board[1] == player.token:
                if self.board[9] == player.token:
                    return player.token
            if self.board[7] == player.token:
                if self.board[3] == player.token:
                    return player.token
            if self.board[2] == player.token:
                if self.board[8] == player.token:
                    return player.token
            if self.board[4] == player.token:
                if self.board[6] == player.token:
                    return player.token
        if self.board[1] ==player.token:
            if self.board[2] == player.token:
                if self.board[3] == player.token:
                    return player.token
            if self.board[4] == player.token:
                if self.board[7] == player.token:
                    return player.token
        if self.board[9] ==player.token:
            if self.board[8] == player.token:
                if self.board[7] == player.token:
                    return player.token
            if self.board[6] == player.token:
                if self.board[3] == player.token:
                    return player.token
        return None
    def is_full(self):
        for i,xo in (self.board).items():
            if xo ==' ':
                return False
        return True
    def is_game_over(self, player):
        print(self.calc_winner(player), player.token)
        if self.calc_winner(player) == player.token:
            return True
        elif self.is_full():
            return True
        return False
    def valid_move(self,number, player):
        if number in ('1','2','3','4','5','6','7','8','9'):
            if self.board[int(number)] == ' ':
                return True
            else:
                print ('Space taken')
                return False
        else:
            print ('Input not valid')
            return False
def main():
    game = Game()
    player1 = Player(1,'O')
    player2 = Player(2,'X')
    players = [player1,player2]
    while True: 
        for player in players:
            print(game)
            valid_move = True
            choice= (input(f'Player {player.player} ({player.token}), please pick a number 1-9: '))
            while game.valid_move(choice,player) == False:
                choice= (input(f'Player {player.player} ({player.token}), please pick a number 1-9: '))
            game.move(choice,player)
            if game.is_game_over(player) == True:
                if game.calc_winner(player) == player.token:
                    print(game)
                    return(f'{game.calc_winner(player)} wins!')
                else:
                    print(game)
                    return('Draw!!')
def play():
    print("Welcome to tic-tac toe. Players take turns placing tokens (an 'O' or 'X') into a 3x3 grid. Whoever gets three in a row first wins.")
    playyn = (input('Would you like to play?\nYes or No?\n')).lower()
    while True:
        if playyn in ['yes','y']:
            print('Of course you do!')
            print(main())
            playyn = (input('Would you like to play, again?\nYes or No?\n')).lower()
        elif playyn in['no','n']:
            return ('Goodbye')
        else:
            print ('What did you say???')
            playyn = (input('Would you like to play?\nYes or No?\n')).lower()
    
print(play())