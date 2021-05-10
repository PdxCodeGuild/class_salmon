import argparse, random

class Piece:
    def __init__(self, color):
        self.color = color

    def __repr__(self):
        return self.color[0].upper()

    def __eq__(self, other):
        if type(other) is Piece:
            if self.color == other.color:
                return True


class GameBoard:
    DEPTH = 6
    WIDTH = 7

    def __init__(self):
        self.board = [['O' for col in range(self.WIDTH)] for row in range(self.DEPTH)]

    def _get_height(self, position):
        for i in range(self.DEPTH-1, -1, -1):
            if self.board[i][position] == 'O':
                return i
        return False # column is full

    def place_piece(self, piece_color, position):
        height = self._get_height(position)
        if type(height) is bool:
            print('Column full. Select another.')
            return False
        self.board[height][position] = Piece(piece_color)

    def print_board(self):
        for row in range(len(self.board)):
            for cell in self.board[row]:
                print(cell, end='|')
            print()
        print()

    def check_win(self):
        for i in range(self.DEPTH-1, -1, -1):
            for j in range(self.WIDTH):
                # check horizontal win
                if j < self.WIDTH-3:
                    chunk = self.board[i][j:j+4]
                    if all(item == self.board[i][j] and item != 'O' for item in chunk):
                        return self.board[i][j]

                # check vertical win
                if i < self.DEPTH-3:
                    chunk = []
                    chunk.append(self.board[i][j])
                    chunk.append(self.board[i+1][j])
                    chunk.append(self.board[i+2][j])
                    chunk.append(self.board[i+3][j])
                    if all(item == self.board[i][j] and item != 'O' for item in chunk):
                        return self.board[i][j]

                # check diagonal wins
                if i < self.DEPTH-3 and j < self.WIDTH-3:
                    chunk = []
                    chunk.append(self.board[i][j:j+4])
                    chunk.append(self.board[i+1][j:j+4])
                    chunk.append(self.board[i+2][j:j+4])
                    chunk.append(self.board[i+3][j:j+4])

                    if chunk[0][0] == chunk[1][1] == chunk[2][2] == chunk[3][3] and chunk[0][0] != 'O':
                        return chunk[0][0]
                    elif chunk[3][0] == chunk[1][2] == chunk[2][1] == chunk[0][3] and chunk[3][0] != 'O':
                        return chunk[3][0]

    def is_full(self):
        for row in self.board:
            if any(item=='O' for item in row):
                return False
        return True

    def game_over(self):
        return self.check_win() or self.is_full()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Connect Four module')
    parser.add_argument('-f', '--file', 
                        help='File path of Connect Four moves you want to evaluate.')
    args = parser.parse_args()

    # File input version
    if args.file:
        with open(args.file, 'r') as f:
            moves = f.read().split()
        
        board = GameBoard()

        for i, move in enumerate(moves):
            current_turn = 'yellow' if i % 2 == 0 else 'red'
            board.place_piece(current_turn, int(move) - 1)

        board.print_board()
        print(board.check_win())

    # 2 player game version
    else:
        while True:
            board = GameBoard()
            player_one = 'yellow'
            player_two = 'red'
            game_round = 1

            while not board.game_over():
                current_player = player_one if game_round % 2 else player_two 

                while True:
                    move = input(f"{current_player}: Enter your move: ").strip().lower()
                    try:
                        move = int(move)
                        if 1 <= move <= 7:
                            move = board.place_piece(current_player, move-1)
                            if type(move) is str:
                                raise IndexError('Invalid column.')
                            board.print_board()
                            break
                        else:
                            raise IndexError('Invalid column.')
                    except (ValueError, IndexError):
                        print("Invalid move. Please choose a column [1-7] that isn't full.")
                game_round += 1

            if not board.is_full():
                print(f"Game over! Winner: {board.check_win()}")
            else:
                print(f"Game over! No one wins!")

            while True:
                play_ag = input("Do you want to play again: ").strip().lower()
                if play_ag in ['yes', 'y', 'no', 'n']:
                    break

            if play_ag in ['no', 'n']:
                break