#game of tic tac toe Lab13
class Player:#proper python has classes in WordCase, first letter cap and run together
    def __init__(self, name = 'hey you', token = 'x' or 'o'):#when the args have something assigned these are defaults
        self.name = name
        self.token = token
     
class Game:
    def __init__(self):
        self.board = {(0,0):'', (1,0):'', (2,0):'', (0,-1):'', (1,-1):'',(2,-1):'',(0,-2):'',(1,-2):'',(2,-2):''}
        # return self.board
    def __repr__(self):#will print (magic funct)
        return self.board
game = Game()#new instance of game
print(game.board)
# print(Game())
# board_structure = [('','',''),('','',''),('','','')] #see data design OOP notebook

# for position in board_structure:
#     position.board

# print(Game.__repr__)#printing the memory location

#to use the class you must create an instance of the class
#example:
#game = Game()
#instances take self as the first argument