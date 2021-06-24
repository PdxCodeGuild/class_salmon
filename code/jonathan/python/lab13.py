class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token  
    def __str__(self):
        return self.name
class Game:
    def __init__(self):
        self.game_board = {
            (0, 0): " ",
            (0, 1): " ",
            (0, 2): " ",
            (1, 0): " ",
            (1, 1): " ",
            (1, 2): " ",
            (2, 0): " ",
            (2, 1): " ",
            (2, 2): " "
            }
    def __repr__(self): 
        # Returns a pretty string representation of the game board
        return f"{self.game_board[(0, 0)]}|{self.game_board[(0, 1)]}|{self.game_board[(0, 2)]}\n{self.game_board[(1, 0)]}|{self.game_board[(1, 1)]}|{self.game_board[(1, 2)]}\n{self.game_board[(2, 0)]}|{self.game_board[(2, 1)]}|{self.game_board[(2, 2)]}"
    def move(self, x, y, player): 
        # Place a player's token character string at a given coordinate (top-left is 0, 0), x is horizontal position, y is vertical position.
        if self.game_board[(x, y)] == " ":
            self.game_board[(x, y)] = player.token
            return True
    def calc_winner(self, player):
        # What token character string has won or None if no one has.
        # for a horizontal line across the top row
        if self.game_board[(0, 0)] == self.game_board[(0, 1)] == self.game_board[(0, 2)] == player.token:
            return True
        # for a horizontal line across the middle row
        elif self.game_board[(1, 0)] == self.game_board[(1, 1)] == self.game_board[(1, 2)] == player.token:
            return True
        # for a horizontal line across the bottom row
        elif self.game_board[(2, 0)] == self.game_board[(2, 1)] == self.game_board[(2, 2)] == player.token:
            return True
        # for a vertical line down the left row
        elif self.game_board[(0, 0)] == self.game_board[(1, 0)] == self.game_board[(2, 0)] == player.token:
            return True
        # for a vertical line down the middle row
        elif self.game_board[(0, 1)] == self.game_board[(1, 1)] == self.game_board[(2, 1)] == player.token:
            return True
        # for a vertical line down the right row
        elif self.game_board[(0, 2)] == self.game_board[(1, 2)] == self.game_board[(2, 2)] == player.token:
            return True
        # for a diagonal line from top left to bottom right
        elif self.game_board[(0, 0)] == self.game_board[(1, 1)] == self.game_board[(2, 2)] == player.token:
            return True
        # for a diagonal line from bottom left to top right
        elif self.game_board[(2, 0)] == self.game_board[(1, 1)] == self.game_board[(0, 2)] == player.token:
            return True
    def is_full(self):
        # Returns true if the game board is full.
        if " " in list(self.game_board.values()):
            return False
        else:
            return True
    def is_game_over(self, player_1, player_2):
        # Returns true if the game board is full or a player has won.
        if self.is_full() or self.calc_winner(player_1) or self.calc_winner(player_2):
            return True
        else: 
            return False
def intro():
    print("First player to go is 'X', 'O' follows.")
    print("Here is the game board, enter the coordinates of the square you would like to place your token.")
    print("0,0|0,1|0,2\n1,0|1,1|1,2\n2,0|2,1|2,2")
def main():
    game = Game()
    player_1 = Player(("Player 1"), "X")
    player_2 = Player(("Player 2"), "O")
    players = [player_1, player_2]
    intro()
    game_counter = 0
    while game.is_game_over(player_1, player_2) == False:
        player = players[game_counter % 2]
        print(f"{player}'s turn.")
        moving = game.move(int(input("Enter the Y axis (up and down) first. ")), int(input("Now the X axis (left and right) please. ")), player)
        if moving == True:
            game_counter += 1
        else:
            print("Space taken, please choose again.")
        print(repr(game))
        if game.is_full() == True and game.calc_winner(player) == True:
            print(f"Better luck next time!")
            break
        elif game.is_full() == True:
            print(f"It's a draw! You'll get them next time!")
            break
    for player in players:
        if game.calc_winner(player) == True:
            print(f"{player} wins!")
    play_again = input("Rematch? Y/N ").upper()
    if play_again == "Y":
        main()
    else:
        print("See you again.")
main()