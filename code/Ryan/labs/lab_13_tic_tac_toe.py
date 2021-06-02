# --------------------------------------------------------------------------------------#

def main(user_inputs):
    pass


class Game:
    def __init__(self): # this is the initializer
        self.board = ["1","2","3","4","5","6","7","8","9"] # these are member variables
        
    # Function to print Tic Tac Toe
    def __repr__(self):
        values = self.board
        line   = "\t{}|{}|{}".format(values[0], values[1], values[2])
        line_2 = "\t{}|{}|{}".format(values[3], values[4], values[5])
        line_3 = "\t{}|{}|{}".format(values[6], values[7], values[8])
        return line + "\n" + line_2 + "\n" + line_3


game = Game()
print(game)

class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token

player1 = Player("player1","x")
player2 = Player("player2","o")


print(player1.name)
print(player1.token)

# --------------------------------------------------------------------------------------#