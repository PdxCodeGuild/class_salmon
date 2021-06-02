board = {'1': '1', '2': '2', '3': '3', '4': '4',
         '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'}


class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token


player1 = Player('Player 1', 'X')
player2 = Player('Player 2', 'O')


class Game:

    def __init__(self, board):
        self.board = board
        self.counter = 0

    def __repr__(self, board):
        print(board['1'] + '|' + board['2'] + '|' + board['3'])
        print('-----')
        print(board['4'] + '|' + board['5'] + '|' + board['6'])
        print('-----')
        print(board['7'] + '|' + board['8'] + '|' + board['9'])

    def move(self, player):
        spot = input(f'{player1.name}, choose a number, 1-9:  ')
        while self.board[spot] == "X" or self.board[spot] == "O":
            print('That spot is already taken! Try again.')
            spot = input(f'{player1.name}, choose a number, 1-9:  ')
        else:
            self.board[spot] = self.board[spot].replace(
                self.board[spot], player1.token)
            self.counter += 1
            self.__repr__(board)

    def calc_winner(self, token):
        if board['1'] == board['2'] == board['3'] == token or board['1'] == board['4'] == board['7'] == token or board['1'] == board['5'] == board['9'] == token or board['2'] == board['5'] == board['8'] == token or board['3'] == board['5'] == board['7'] == token or board['3'] == board['6'] == board['9'] == token or board['4'] == board['5'] == board['6'] == token or board['7'] == board['8'] == board['9'] == token:
            return True

    def is_full(self):
        if self.counter == 9:
            return True

    def is_game_over(self):
        if self.counter == 9 or self.calc_winner(player1.token) == True:
            return True
        else:
            return False


def main(player, token):
    game1 = Game(board)

    while True:
        game1.__repr__(board)

        game1.move(player)

        game1.calc_winner(token)
        if game1.calc_winner(token) == True:
            print(f'{token}\'s win!')
            again = input(f'Game Over. Play again? Enter y or n:  ')
            if again == 'y':
                main(player, token)
            if again == 'n':
                break

        game1.is_full()

        game1.is_game_over()
        if game1.is_game_over() == True:
            again = input(f'Game Over. Play again? Enter y or n:  ')
            if again == 'y':
                game1 = Game(board)
            if again == 'n':
                break


main(player1, player1.token)
