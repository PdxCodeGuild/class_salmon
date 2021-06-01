#game of tic tac toe Lab13
token1 = input('Select X or O for player 1').lower()
token2 = 'o' if token1 == 'x' else 'x'
# print(token1)
# print(token2)
class Player:#proper python has classes in WordCase, first letter cap and run together
    def __init__(self, token1 = 'x', token2 = 'o', name1 = 'hey you', name2 = 'sure pal'):#when the args have something assigned these are defaults
        self.token1 = token1
        self.token2 = token2
        self.name1 = name1
        self.name2 = name2
        # self.token = token#hmm can I assign two default values? It does not appear so
     
class Game:
    def __init__(self):
        #dictionary cannot take lists as keys. Below the dictionary takes tuples as coordinates/keys
        self.position = {(0,0):'-', (1,0):'-', (2,0):'-', (0,-1):'-', (1,-1):'-',(2,-1):'-',(0,-2):'-',(1,-2):'-',(2,-2):'-'}
        self.board = (f'Welcome to Thunderdome Tic Tac Toe \n          {self.position[(0,0)]}|{self.position[(1,0)]}|{self.position[(2,0)]}\n          {self.position[(0,-1)]}|{self.position[(1,-1)]}|{self.position[(2,-1)]}\n          {self.position[(0,-2)]}|{self.position[(1,-2)]}|{self.position[(2,-2)]}')
        
    def __repr__(self):#will print (magic funct)
        return self.board
    def move(self, x, y, player):#I will need to assign x or o to the player attribute somewhere
        self.position[(x,y)] = #maybe this should be token?


game = Game()#new instance of game
player1 = Player(token1, token2)
player2 = Player(token2, token2)
print(player1.token1)#this is printing x
print(player2.token2)#this is also printing x
#print(game.move(0,0,player))
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