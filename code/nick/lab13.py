#game of tic tac toe Lab13
class Player:#proper python has classes in WordCase, first letter cap and run together
    def __init__(self, name = 'hey you', token = 'x' or 'o'):#when the args have something assigned these are defaults
        self.name = name
        self.token = token#hmm can I assign two default values?
     
class Game:
    def __init__(self):
        #dictionary cannot take lists as keys. Below the dictionary takes tuples as coordinates/keys
        self.board = {(0,0):'', (1,0):'', (2,0):'', (0,-1):'', (1,-1):'',(2,-1):'',(0,-2):'',(1,-2):'',(2,-2):''}
        # return self.board
    def __repr__(self):#will print (magic funct)
        return self.board
    def move(self, x, y, player):#I will need to assign x or o to the player attribute somewhere
        self.board[(x,y)] = player


game = Game()#new instance of game
print(game.board)
# print(Game())
# board_structure = [('','',''),('','',''),('','','')] #see data design OOP notebook

# for position in board_structure:
#     position.board

# print(Game.__repr__)#printing the memory location
#Stackoverflow thoughts... on dictionary as an attribute
#to use the class you must create an instance of the class
#example:
#game = Game()
#instances take self as the first argument
#It is possible to do it that way, but if it were me, I would create a dictionary of attributes that could be updated in a function for each command: 
def __init__(self):     
    self.Attributes = {'Color': '','Make': '','Model': ''} 
    #Then update it with a function: 
def _updateColor(self):     
    currentColor = self.Attributes['Color'] 
    #This would get a list of colors     
    # Do stuff to specify a new color     
    self.Attributes['Color'] = newColor    