# Lab 13: Tic-Tac-Toe
# Tic Tac Toe is a game. Players take turns placing tokens (a 'O' or 'X') into a 3x3 grid. Whoever gets three in a row first wins.

# You will write a Player class and Game class to model Tic Tac Toe, and a function main that models gameplay taking in user inputs through REPL.

# The Player class has the following properties:
class Player:

# name = player name
# token = 'X' or 'O'
    def __init__(self, name, token):
        self.name = name
        self.token = token
    
    def __str__(self):
        return self.token

# The Game class has the following properties:
class Game:

    # board = your representation of the board
    # You can represent the board however you like, such as a 2D list, tuples, or dictionary.

    def __init__(self):
        self.board = {
            (0, 0): " ", (0, 1): " ", (0, 2): " ",
            (1, 0): " ", (1, 1): " ", (1, 2): " ",
            (2, 0): " ", (2, 1): " ", (2, 2): " "}


    # The Game class has the following methods:
    # __repr__() Returns a pretty string representation of the game board
    # >>> print(board)
    # X| | 
    # O|X|O
    #  | | 
    def __repr__(self):
        return f'''
            {self.board[(0, 0)]}|{self.board[(1, 0)]}|{self.board[(2, 0)]}
            {self.board[(0, 1)]}|{self.board[(1, 1)]}|{self.board[(2, 1)]}
            {self.board[(0, 2)]}|{self.board[(1, 2)]}|{self.board[(2, 2)]}
            '''

    # move(x, y, player) Place a player's token character string at a given coordinate (top-left is 0, 0), x is horizontal position, y is vertical position.
    # >>> board.move(2, 1, player_1)
    #  | | 
    #  | |X
    #  | | 

    def move(self, x, y, player):
        self.x = x
        self.y = y
        
        self.board[input] = player.token
        # self.input = input
        # self.player = player

        # Add the player move to players list
        if player.token == "x":
            x_moves.append(self.input)
            self.board.update({f"{self.input}": "x"})
        elif player.token == "o":
            o_moves.append(self.input)
            self.board.update({f"{self.input}": "o"})        
        
        # possible_positions.remove(str(self.input))

        return 

    # calc_winner() What token character string has won or None if no one has.
    # X| | 
    # O|X|O
    #  | |X
    # >>> board.calc_winner()
    # X
    def calc_winner(self, player1, player2):
        # self.player1 = Player.move
        print(player1)

        if (("0" in x_moves and "1" in x_moves and "2" in x_moves) or 
            ("3" in x_moves and "4" in x_moves and "5" in x_moves) or 
            ("6" in x_moves and "7" in x_moves and "8" in x_moves) or 
            ("0" in x_moves and "3" in x_moves and "6" in x_moves) or 
            ("1" in x_moves and "4" in x_moves and "7" in x_moves) or
            ("2" in x_moves and "5" in x_moves and "8" in x_moves) or 
            ("0" in x_moves and "4" in x_moves and "8" in x_moves) or 
            ("2" in x_moves and "4" in x_moves and "6" in x_moves)):
            turn_counter = 9
            return turn_counter

        if (("0" in o_moves and "1" in o_moves and "2" in o_moves) or 
            ("3" in o_moves and "4" in o_moves and "5" in o_moves) or 
            ("6" in o_moves and "7" in o_moves and "8" in o_moves) or 
            ("0" in o_moves and "3" in o_moves and "6" in o_moves) or 
            ("1" in o_moves and "4" in o_moves and "7" in o_moves) or
            ("2" in o_moves and "5" in o_moves and "8" in o_moves) or 
            ("0" in o_moves and "4" in o_moves and "8" in o_moves) or 
            ("2" in o_moves and "4" in o_moves and "6" in o_moves)):
            turn_counter = 9
            return turn_counter
        return False

    # is_full() Returns true if the game board is full.
    # X|O|X
    # X|X|O
    # O|O|X
    # >>> board.is_full()
    # True
    def is_full(self, turn_counter):
        if turn_counter == 9:
            return True
        return False

    # is_game_over() Returns true if the game board is full or a player has won.
    # X|O|X
    # X|X|O
    # O|O|X
    # >>> board.is_game_over()
    # True
    def is_game_over(self):
        return self.calc_winner() is not None or self.is_full()
        # if game.is_full == True:
        #     return True
        # return False

# X|O|
#  | |X
#  | |
# >>> board.is_game_over()
# False
    # List of all moves player x made
x_moves = []

# List of all moves player o made
o_moves = []

def main():
# Define the players
    player1 = Player("player1","x")
    player2 = Player("player2","o")

    # Add the players to a list so the turn counter can loop
    players = [player1, player2]

    # List all possible positions
    possible_positions = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]

    # List of all moves player x made


    # Start the game
    game = Game()

    # Start turn counter
    turn_counter = 0

    while turn_counter != 9:
        # Display the board
        print(game)

        # Player turns are passed back and forth using modulus. 
        player = players[turn_counter % len(players)]
        print(f"{player}'s turn.")
        
        # Input the coordinate for where to place player token
        player_move = input("Enter a number: ").strip()
        # check if player_move is valid
        game.move(player_move, player)

        # Add 1 to the counter to pass turn
        turn_counter += 1

        winner = game.calc_winner(player1, player2)
        if winner is not None:
            print(winner + ' won the game!')
            break
        elif game.is_full(turn_counter): # Check if the board is full
            print("tie game. game over")
            break

        # Check if the game is over
        # if game.is_game_over():
        #     break


        player = Player.moves
        
        # List moves
        print("X moves", player1.moves)
        print("O moves", player2.moves)

        print(possible_positions)
        print(turn_counter)
        

play_again = 'yes'
while play_again == 'yes':
    main()
    play_again = input('play again? ')

