class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token


player1 = Player('Player 1', 'X')
player2 = Player('Player 2', 'O')
players_list = [player1, player2]


class Game:
    def __init__(self):
        self.counter = 0
        self.board = {'1': '1', '2': '2', '3': '3', '4': '4',
                      '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'}

    def __repr__(self):
        return '\n' + self.board['1'] + '|' + self.board['2'] + '|' + self.board['3'] + '\n' + '-----' + '\n' + self.board['4'] + '|' + self.board['5'] + '|' + self.board['6'] + '\n' + '-----' + '\n' + self.board['7'] + '|' + self.board['8'] + '|' + self.board['9']

    def move(self, player):
        spot = input(f'{player.name}, choose a number, 1-9:  ')
        while self.board[spot] == "X" or self.board[spot] == "O":
            print('That spot is already taken! Try again.')
            spot = input(f'{player.name}, choose a number, 1-9:  ')
        else:
            self.board[spot] = player.token
            # self.board[spot] = self.board[spot].replace(
            #    self.board[spot], player.token)
            self.counter += 1

    def calc_winner(self, token):
        if self.board['1'] == self.board['2'] == self.board['3'] == token or self.board['1'] == self.board['4'] == self.board['7'] == token or self.board['1'] == self.board['5'] == self.board['9'] == token or self.board['2'] == self.board['5'] == self.board['8'] == token or self.board['3'] == self.board['5'] == self.board['7'] == token or self.board['3'] == self.board['6'] == self.board['9'] == token or self.board['4'] == self.board['5'] == self.board['6'] == token or self.board['7'] == self.board['8'] == self.board['9'] == token:
            return True
        else:
            return False

    def is_game_over(self, player):
        if self.calc_winner(player.token) == True:
            return True

        elif self.counter == 9:
            print('\n\nTie Game!')
            return True

        return False


def main():

    done = False
    game1 = Game()

    while done == False:
        for p in players_list:
            print(game1)

            game1.move(p)

            done = game1.is_game_over(p)
            if done == True:
                break
    print(game1, '\nGame Over!')

    again = input(f'Play again? Enter y or n:  ')
    if again == 'y':
        main()


main()
