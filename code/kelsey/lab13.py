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
    player_1 = Player((input(f'\nEnter Player 1 name: ')), 'X')
    player_2 = Player((input(f'Enter Player 2 name: ')), 'O')
    players = [player_1, player_2]
    print('\nWelcome to Tic-Tac-Toe! \n\nPlayer 1 is X; Player 2 is O. X starts the game. Take turns placing your token on the game board. The object of the game is to have three of your tokens line up either vertically, horizontally, or diagonally. The game is over once a player wins, or the board is full. ')
    counter = 0
    while game.is_game_over(player_1, player_2) == False:
        player = players[counter % 2]
        print(f'\n{player}\'s turn \n')
        valid_move = game.move(int(input('From far left, move RIGHT (0,1,2) space(s): ')), int(input('From top, move DOWN (0,1,2) space(s): ')), player)
        if valid_move == True:
            counter += 1
        else:
            print('\nNot a valid move. Please choose again.')
        print(f'\n{repr(game)}')
        if game.is_full() == True and game.calc_winner(player) == True:
            print(f'\nGame over.')
            break
        elif game.is_full() == True:
            print(f'\nDraw. Game over.\n')
            break
    for player in players:
        if game.calc_winner(player) == True:
            print(f'\n{player} wins!\n')
    play_again = input('Would you like to play again? Y/N ').upper()
    if play_again == 'Y':
        main()
    else:
        print('\nThanks for playing!\n')
        

main()