board = {'1': '1', '2': '2', '3': '3', '4': '4',
         '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'}


print('1' + '|' + '2' + '|' + '3')
print('-+-+-')
print('4' + '|' + '5' + '|' + '6')
print('-+-+-')
print('7' + '|' + '8' + '|' + '9')


def __repr__(self):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-----')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-----')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])


# __repr__(board)


def move(self, move, player):
    if board[str(move)] == ' ':
        board[str(move)] = player

    else:
        print('That space is already taken. Try again: ')


player1 = input('Player 1, choose a number, 1-9:  ')
move(board, player1, 'X')
__repr__(board)

player2 = input('Player 2, choose a number, 1-9:  ')
move(board, player2, 'O')
__repr__(board)
#####################print prompt for user move again################


'''


class Player:
    def __init__(self):
        self.name =
        self.token = 'X'



class Game:
    print(board)

    def __init__(self):
        self.board = board
        board = [' ',' ',' '],[' ',' ',' '],[' ',' ',' ']

       # for i in board:
       #     x = '|'.join(i)
       #     print(x)

    def move(self, x, y, player):

    def calc_winner(self):

    def is_full(self):
        # if len(self.board) == 9:
            # True
    def is_game_over():
        # if len(self.board) == 9 or (win)
            # True



'''

# def main():
print('1' + '|' + '2' + '|' + '3')
print('-+-+-')
print('4' + '|' + '5' + '|' + '6')
print('-+-+-')
print('7' + '|' + '8' + '|' + '9')

#spots = True
# while spots == True:
#    for k in board.keys():
#        if k != ' ':
#            pass
#        else:
#            break
player1 = input('Player 1, choose a number, 1-9:  ')
move(board, player1, 'X')
__repr__(board)

player2 = input('Player 2, choose a number, 1-9:  ')
move(board, player2, 'O')
__repr__(board)
