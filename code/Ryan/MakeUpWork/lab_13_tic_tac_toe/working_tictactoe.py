import click
class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token
    
    def __str__(self):
        return self.token

class Game:
    def __init__(self):
        self.board = {
            "0": 0, "1": 1, "2": 2, 
            "3": 3, "4": 4, "5": 5,
            "6": 6, "7": 7, "8": 8
            }

    def __repr__(self):
        return f"""
        \t{self.board["0"]}|{self.board["1"]}|{self.board["2"]}
        \t{self.board["3"]}|{self.board["4"]}|{self.board["5"]}
        \t{self.board["6"]}|{self.board["7"]}|{self.board["8"]}
        """
    def move(self, input, player):
        self.board[input] = player.token
        self.input = input
        self.player = player

        if player.token == "x":
            x_moves.append(self.input)
            self.board.update({f"{self.input}": "x"})
        elif player.token == "o":
            o_moves.append(self.input)
            self.board.update({f"{self.input}": "o"})        
        
        # possible_positions.remove(str(self.input))

        return 

    def calc_winner(self, player_name=None):

        if ((0 in x_moves and 1 in x_moves and 2 in x_moves) or 
            (3 in x_moves and 4 in x_moves and 5 in x_moves) or 
            (6 in x_moves and 7 in x_moves and 8 in x_moves) or 
            (0 in x_moves and 3 in x_moves and 6 in x_moves) or 
            (1 in x_moves and 4 in x_moves and 7 in x_moves) or
            (2 in x_moves and 5 in x_moves and 8 in x_moves) or 
            (0 in x_moves and 4 in x_moves and 8 in x_moves) or 
            (2 in x_moves and 4 in x_moves and 6 in x_moves)):
            return True

        if ((0 in o_moves and 1 in o_moves and 2 in o_moves) or 
            (3 in o_moves and 4 in o_moves and 5 in o_moves) or 
            (6 in o_moves and 7 in o_moves and 8 in o_moves) or 
            (0 in o_moves and 3 in o_moves and 6 in o_moves) or 
            (1 in o_moves and 4 in o_moves and 7 in o_moves) or
            (2 in o_moves and 5 in o_moves and 8 in o_moves) or 
            (0 in o_moves and 4 in o_moves and 8 in o_moves) or 
            (2 in o_moves and 4 in o_moves and 6 in o_moves)):
            return True

        return False

    def is_full(self, counter):
        print(f"turn: {counter}")
        if counter == 9:
            return True

    def is_game_over(self):
        if self.calc_winner():
            return True

def clrscr():
    click.clear()

    print(49 * "*")
    print(18 * "-" + " TIC-TAC-TOE " + 18 * "-")
    print(49 * "*")

def main(turn_counter, x_moves, o_moves, possible_positions):
    clrscr()

    player1 = Player(input("Whoever wants to be 'x', enter a name: "), "x")
    player2 = Player(input("Whoever wants to be 'o', enter a name: "), "o")
    players = [player1, player2]

    print(f"\nVery Well, {player1.name} is playing as {player1.token}, and {player2.name} is stuck as {player2.token}.\nLet's start this...")

    game = Game()

    while True:
        clrscr()
        print(game)
        player = players[turn_counter % len(players)]
        print(f"{player.name}'s turn.")

        game.move(int(input("Enter a number: ")), player)
        game.calc_winner(player)
        game.is_full(turn_counter)

        turn_counter += 1

        if game.is_game_over():
            print(game)
            print(f'Player {player} wins!')
            break
        elif game.is_full(turn_counter):
            clrscr()
            print(game)
            print(f"Tie")
            break
            
play_again = 'y'
while play_again == 'y':
    x_moves = []
    o_moves = []
    possible_positions = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
    turn_counter = 0


    main(turn_counter, x_moves, o_moves, possible_positions)
    play_again = input('Game Over. Play again? (y/n): ')