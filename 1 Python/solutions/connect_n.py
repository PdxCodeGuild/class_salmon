# connect_n.py 
# A combination of Tic Tac Toe and Connect Four: a two player game where to first player to get N in a row wins!
# Constraints:  2 <= N <= 8, 3x3 <= board_size <= 8x8
# Default: N=5, board=8x8

import argparse, random

class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token

    def __eq__(self, other):
        if type(other) is Player:
            return self.token == other.token

    def __repr__(self):
        return self.token

class Board:

    def __init__(self, n, size):
        self.DEPTH = size
        self.WIDTH = size
        self.n = n
        self.board = [[str(i+j*self.WIDTH+1).zfill(2) for i in range(self.WIDTH)] for j in range(self.DEPTH)]

    def __repr__(self):
        ret = ''
        for row in self.board:
            for cell in row:
                ret += str(cell) + '|'
            ret += '\n'
        return ret

    def place_token(self, x, y, token):
        if type(self.board[y][x]) is Player:
            return 'Invalid move. Space taken.'
        else:
            self.board[y][x] = token

    def calc_winner(self):
        for i in range(self.DEPTH):
            for j in range(self.WIDTH):
                # check horizontal wins
                if (j < self.WIDTH - self.n + 1):
                    chunk = self.board[i][j:j+self.n]
                    if all(item == self.board[i][j] and type(item) is Player for item in chunk):
                        return self.board[i][j].name

                # check vertical wins
                if (i < self.DEPTH - self.n + 1):
                    chunk = [self.board[i+k][j] for k in range(self.n)]
                    if all(item == self.board[i][j] and type(item) is Player for item in chunk):
                        return self.board[i][j]


                # check diagonal wins
                if (i < self.DEPTH - self.n + 1 and j < self.WIDTH - self.n + 1):
                    chunk = [self.board[i+k][j:j+self.n] for k in range(self.n)]
                    left_diag = True
                    right_diag = True
                    for k in range(self.n):
                        if not left_diag and not right_diag :
                            continue
                        if chunk[k][k] != chunk[0][0] or not type(chunk[k][k]) is Player:
                            left_diag = False
                        if chunk[self.n-k-1][k] != chunk[self.n-1][0] or not type(chunk[self.n-k-1][k]) is Player:
                            right_diag = False
                    if left_diag:
                        return chunk[0][0]
                    if right_diag:
                        return chunk[self.n-1][0]

    def is_full(self):
        for row in self.board:
            if any(not type(item) is Player for item in row):
                return False
        return True

    def is_game_over(self):
        return self.calc_winner() or self.is_full()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Connect N Game')
    parser.add_argument('-n', type=int, choices=range(2, 9), help='Number to connect to win.')
    parser.add_argument('-s', '--boardsize', type=int, choices=range(3, 9), help='Size of game board (size x size)')
    args = parser.parse_args()

    while True:
        N = args.n if args.n else 5             # default N=5
        SIZE = args.boardsize if args.boardsize else 8    # default 8x8 board
        board = Board(N, SIZE)
        grid_coord = {}
        for y in range(board.DEPTH):
            for x in range(board.WIDTH):
                grid_coord[x+1+y*board.WIDTH] = (x, y)
        # print(N, SIZE)
        # print(grid_coord)

        player_one = Player(input("Player one: "), '██')
        player_two = Player(input("Player two: "), '░░')
        game_round = 1

        while not board.is_game_over():
            current_player = player_one if game_round % 2 else player_two 

            while True:
                move = input(f"{current_player.name}: Enter your move: ").strip()
                try:
                    move = int(move)
                    if 1 <= move <= SIZE**2:
                        x, y = grid_coord[move]
                        move = board.place_token(x, y, current_player)
                        if type(move) is str:
                            raise IndexError('Invalid move.')
                        print(board)
                        game_round += 1
                        break
                    else:
                        raise IndexError('Invalid move.')
                except (ValueError, IndexError):
                    # try:
                    #   x, y = move.split(',')
                    # except ValueError, IndexError:
                        print(f"Invalid move. Please choose a square [1-{SIZE**2}] that isn't full.")

        if not board.is_full():
            print(f"Game over! Winner: {board.calc_winner()}")
        else:
            print(f"Game over! Tie!")

        while True:
            play_ag = input("Do you want to play again: ").strip().lower()
            if play_ag in ['yes', 'y', 'no', 'n']:
                break

        if play_ag in ['no', 'n']:
            break      