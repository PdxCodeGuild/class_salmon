# Lab 13: Tic-Tac-Toe

class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token
    
    def __str__(self):
        return self.name
        
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
        if self.board[(y, x)] == ' ':
            self.board[(y, x)] = player.token
            return True
        
    def calc_winner(self, player):
        if self.board[(0, 0)] == self.board[(0, 1)] == self.board[(0, 2)] == player.token:
            return True
        elif self.board[(0, 1)] == self.board[(1, 1)] == self.board[(2, 1)] == player.token:
            return  True
        elif self.board[(0, 2)] == self.board[(1, 2)] == self.board[(2, 2)] == player.token:
            return  True
        elif self.board[(0, 0)] == self.board[(1, 0)] == self.board[(2, 0)] == player.token:
            return  True
        elif self.board[(1, 0)] == self.board[(1, 1)] == self.board[(1, 2)] == player.token:
            return  True
        elif self.board[(2, 0)] == self.board[(2, 1)] == self.board[(2, 2)] == player.token:
            return  True
        elif self.board[(0, 0)] == self.board[(1, 1)] == self.board[(2, 2)] == player.token:
            return  True
        elif self.board[(0, 2)] == self.board[(1, 1)] == self.board[(2, 0)] == player.token:
            return  True

    def is_full(self):
        if ' ' in list(self.board.values()):
            return False
        else:
            return True

    def is_game_over(self, player_1, player_2):
        if self.is_full() or self.calc_winner(player_1) or self.calc_winner(player_2):
            return True
        else: 
            return False

def main():
    game = Game()
    player_1 = Player((input(f'Enter Player 1 name: ')), 'X')
    player_2 = Player((input(f'Enter Player 2 name: ')), 'O')
    players = [player_1, player_2]
    print('Start New Game')
    counter = 0
    while game.is_game_over(player_1, player_2) == False:
        player = players[counter % 2]
        print(f'{player}, your move')
        valid_move = game.move(int(input('(from top left) move right _ space(s): ')), int(input('(from top left) move down _ space(s): ')), player)
        if valid_move == True:
            counter += 1
        else:
            print('\nNot a valid move. Please choose again.\n')
        print(repr(game))
    for player in players:
        if game.calc_winner(player) == True:
            print(f'{player} wins!')
    play_again = input('Would you like to play again? Y/N ').upper()
    if play_again == 'Y':
        main()
    else:
        print('Thanks for playing!')
        

main()