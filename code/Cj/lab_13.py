def isfloat(x):
    try:
        x = float(x)
        return True
    except:
        return False

class player:
    def __init__(self):
        self.name = input('Please enter your name: ')
        self.token = input('x\'s or o\'s: ').lower()

class board:
    def __init__(self):
        self.board = {0.0: ' ', 1.0: ' ', 2.0: ' ',
        0.1: ' ', 1.1: ' ', 2.1: ' ',
        0.2: ' ', 1.2: ' ', 2.2: ' '}
        self.winner = 'The Cat'
    def __repr__(self):
        output = ''
        return f'''
         _ _ _
        |{self.board[0.0]}|{self.board[1.0]}|{self.board[2.0]}|
         -+-+-
        |{self.board[0.1]}|{self.board[1.1]}|{self.board[2.1]}|
         -+-+-
        |{self.board[0.2]}|{self.board[1.2]}|{self.board[2.2]}|
         ‾ ‾ ‾
        '''

    def move(self, player):
        while True:
            coord = input('Enter x.y coordinates: ')
            if isfloat(coord):
                coordinates = coord.split('.')
                x = int(coordinates[0])
                y = int(coordinates[1])
                coord = float(coord)
            else:
                print('Enter a decimal value to represent a coordinate!')
                continue
            if x > 2 or y > 2:
                print('Coordinates do not exist! ')
                continue
            if self.board[coord] != ' ':
                print('Space occupied!')
                continue
            else:
                self.board[coord] = player.token
                break

    def calc_winner(self):
        if self.board[0.0] == self.board[1.0] and self.board[0.0] == self.board[2.0] and self.board[1.0] == self.board[2.0] and self.board[0.0] != ' ':
            self.winner = self.board[1.0]
            return True
        elif self.board[0.1] == self.board[1.1] and self.board[0.1] == self.board[2.1] and self.board[1.1] == self.board[2.1] and self.board[0.1] != ' ':
            self.winner = self.board[1.1]
            return True
        elif self.board[0.2] == self.board[1.2] and self.board[0.2] == self.board[2.2] and self.board[1.2] == self.board[2.2] and self.board[0.2] != ' ':
            self.winner = self.board[1.2]
            return True
        elif self.board[0.0] == self.board[0.1] and self.board[0.0] == self.board[0.2] and self.board[0.1] == self.board[0.2] and self.board[0.2] != ' ':
            self.winner = self.board[0.2]
            return True
        elif self.board[1.0] == self.board[1.1] and self.board[1.0] == self.board[1.2] and self.board[1.1] == self.board[1.2] and self.board[1.0] != ' ':
            self.winner = self.board[1.2]
            return True
        elif self.board[2.0] == self.board[2.1] and self.board[2.0] == self.board[2.2] and self.board[2.1] == self.board[2.2]and self.board[2.0] != ' ':
            self.winner = self.board[2.0]
            return True
        elif self.board[0.0] == self.board[1.1] and self.board[0.0] == self.board[2.2] and self.board[1.1] == self.board[2.2]and self.board[0.0] != ' ':
            self.winner = self.board[0.0]
            return True
        elif self.board[0.2] == self.board[1.1] and self.board[0.2] == self.board[2.0] and self.board[1.1] == self.board[2.0]and self.board[0.2] != ' ':
            self.winner = self.board[0.2]
            return True
        else:
            return False

    def isfull(self):
        for k, v in self.board.items():
            if v == ' ':
                return False
        return True
    
    def is_over(self):
        if self.isfull() or self.calc_winner():
            return True
        else:
            return False

class Menu:
    def __init__(self):
        self.main = '''
        Welcome to Tic-Tac-Toe!

        Please make a selection from the following menu:

        1. Start Game!

        2. How to play.

        3. Exit.

        Enter: '''

        self.rules = '''
         RULES FOR TIC-TAC-TOE

        The game is played on a 3 by 3 grid of squares. 

        You are X or O and your opponent is the opposite. Players take turns putting their tokens in empty squares.

        Enter your move by entering the x.y coordinates of the square you would like to place your token in. 
        
        x represents the horizontal coordinate and y represents the vertical The top left corner being 0.0 and the center square being 1.1

        The first player to get 3 of their tokens in a row (up, down, across, or diagonally) is the winner.

        When all of the squares are full, the game is over. If neither player placed 3 of their tokens in a row, the cat wins (Game ended in a draw).
        '''

        self.retur = '''
        1. Return to main menu

        2. Exit

        Enter: '''
        self.err = 'Error! Please make a valid selection: '

        self.nav = '0'
    
    def valid(self, menu):
        self.nav = str(self.nav)
        if self.nav.isnumeric():
            self.nav = int(self.nav)
        else:
            return False
        if menu == self.retur:
            if self.nav < 1 or self.nav > 2:
                return False
            else:
                return self.nav
        elif menu == self.main:
            if self.nav < 1 or self.nav > 3:
                return False
            else:
                return self.nav
    def error(self):
        self.main = self.main.replace('Enter: ', self.err)
        self.retur = self.retur.replace('Enter: ', self.err)

    # def correct_error(self):
    #     self.main = self.main.replace(self.err, 'Enter: ')
    #     self.retur = self.retur.replace(self.error, 'Enter: ')

    def main_(self):
        while not self.valid(self.main):
            self.nav = input(f'{self.main}')
            if not self.valid(self.main):
                self.error()
        return self.nav
        

    def return_(self):
        self.nav = '0'
        while not self.valid(self.retur):
            self.nav = input(f'{self.retur}')
            if not self.valid(self.retur):
                self.error()
        return self.nav
        
    def play_game(self):
        print('Okay, lets start!')
        game = board()
        player_1 = player()
        player_2 = player()
        print(game.__repr__())
        while True:
            print(f'{player_1.name}\'s turn.')
            game.move(player_1)
            print(game.__repr__())
            if game.is_over():
                break
            print(f'{player_2.name}\'s turn.')
            game.move(player_2)
            print(game.__repr__())
            if game.is_over():
                break
        print('Game over! ')
        if game.winner == player_1.token:
            winner = player_1.name
        elif game.winner == player_2.token:
            winner = player_2.name
        else:
            winner = game.winner
        print(f'The winner was {winner}.')

def run_program():
    menu = Menu()
    while True:
        menu.nav = '0'
        menu_select = menu.main_()
        if menu_select == 1:
            menu.play_game()
            play_again = input('Do you want to play again(y/n)?: ').lower()
            if play_again == 'y':
                continue
            else:
                break
        elif menu_select == 2:
            print(menu.rules)
            menu_select = menu.return_()
            if menu_select == 2:
                exit()
            else:
                continue
        elif menu_select == 3:
            exit()
    print('Thank you for playing! Peace and love. <3')

run_program()