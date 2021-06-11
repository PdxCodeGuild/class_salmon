# Lab 13: Tic-Tac-Toe
# Tic Tac Toe is a game. Players take turns placing tokens (a 'O' or 'X') into a 3x3 grid. Whoever gets three in a row first wins.

# You will write a Player class and Game class to model Tic Tac Toe, and a function main that models gameplay taking in user inputs through REPL.
import random
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
            "0": "0", "1": "1", "2": "2", 
            "3": "3", "4": "4", "5": "5",
            "6": "6", "7": "7", "8": "8"
            }

# The Game class has the following methods:

# __repr__() Returns a pretty string representation of the game board
# >>> print(board)
# X| | 
# O|X|O
#  | | 
    def __repr__(self):
        return f"""
        \t{self.board["0"]}|{self.board["1"]}|{self.board["2"]}
        \t{self.board["3"]}|{self.board["4"]}|{self.board["5"]}
        \t{self.board["6"]}|{self.board["7"]}|{self.board["8"]}
        """

# move(x, y, player) Place a player's token character string at a given coordinate (top-left is 0, 0), x is horizontal position, y is vertical position.
# >>> board.move(2, 1, player_1)
#  | | 
#  | |X
#  | | 
    def move(self, input, player):
        self.board[input] = player.token
        self.input = input
        self.player = player

        # Add the player move to players list
        if player.token == "x":
            x_moves.append(self.input)
            self.board.update({f"{self.input}": "x"})
        elif player.token == "o":
            o_moves.append(self.input)
            self.board.update({f"{self.input}": "o"})        
        
        possible_positions.remove(str(self.input))

        return 

# calc_winner() What token character string has won or None if no one has.
# X| | 
# O|X|O
#  | |X
# >>> board.calc_winner()
# X
    def calc_winner(self, player_name):
        self.player_name = player_name

        if (("0" in x_moves and "1" in x_moves and "2" in x_moves) or 
            ("3" in x_moves and "4" in x_moves and "5" in x_moves) or 
            ("6" in x_moves and "7" in x_moves and "8" in x_moves) or 
            ("0" in x_moves and "3" in x_moves and "6" in x_moves) or 
            ("1" in x_moves and "4" in x_moves and "7" in x_moves) or
            ("2" in x_moves and "5" in x_moves and "8" in x_moves) or 
            ("0" in x_moves and "4" in x_moves and "8" in x_moves) or 
            ("2" in x_moves and "4" in x_moves and "6" in x_moves)):
            return True
        return False

# is_full() Returns true if the game board is full.
# X|O|X
# X|X|O
# O|O|X
# >>> board.is_full()
# True
    def is_full(self):
        self.turn_counter = self
        if self.turn_counter == 9:
            return True
        return False

# is_game_over() Returns true if the game board is full or a player has won.
# X|O|X
# X|X|O
# O|O|X
# >>> board.is_game_over()
# True
    def is_game_over():
        if game.is_full == True:
            return True
        return False

# X|O|
#  | |X
#  | |
# >>> board.is_game_over()
# False

# Define the players
player1 = Player("player1","x")
player2 = Player("player2","o")

# Add the players to a list so the turn counter can loop
players = [player1, player2]

# List all possible positions
possible_positions = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]

# List of all moves player x made
x_moves = []

# List of all moves player o made
o_moves = []

# Start the game
game = Game()

# Start turn counter
turn_counter = 0

while True:
    # Display the board
    print(game)

    # Player turns are passed back and forth using modulus. 
    player = players[turn_counter % len(players)]
    print(f"{player}'s turn.")
    
    # Input the coordinate for where to place player token
    game.move(int(input("Enter a number: ")), player)

    # Add 1 to the counter to pass turn
    turn_counter += 1

    # Check if the game is over
    
    # Check if the board is full
    game.is_full()
    
    # List moves
    print("X moves", x_moves)
    print("O moves", o_moves)

    print(possible_positions)
    print(turn_counter)
    

