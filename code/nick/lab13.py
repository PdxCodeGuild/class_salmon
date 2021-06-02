#game of tic tac toe Lab13
#token = input('Select X or O for player 1').lower()
#name = input('Type your name ').lower()
# token2 = 'o' if token1 == 'x' else 'x'
# print(token1)
# print(token2)
class Player:#proper python has classes in WordCase, first letter cap and run together
    def __init__(self, token, name):#when the args have something assigned these are defaults
        self.token = token
        self.name = name
        # self.token = token#hmm can I assign two default values? It does not appear so
     
class Game:
    def __init__(self):
        #dictionary cannot take lists as keys. Below the dictionary takes tuples as coordinates/keys
        self.board = {(0,0):'-', (1,0):'-', (2,0):'-', (0,-1):'-', (1,-1):'-',(2,-1):'-',(0,-2):'-',(1,-2):'-',(2,-2):'-'}
        
        
    def __repr__(self):#will print (magic funct)
        return (f'''Welcome to Thunderdome Tic Tac Toe          
        {self.board[(0,0)]}|{self.board[(1,0)]}|{self.board[(2,0)]}         
        {self.board[(0,-1)]}|{self.board[(1,-1)]}|{self.board[(2,-1)]}         
        {self.board[(0,-2)]}|{self.board[(1,-2)]}|{self.board[(2,-2)]}\n''')#I keep getting a ghost arrow >
    
    def move(self, x, y, player):#I will need to assign x or o to the player attribute somewhere
        if self.board[(x,y)] == '-':
            self.board[(x,y)] = player
        #not sure if I should break or there is something better
        #print(player)
    def calc_winner(self):
        self.winners = [
            [self.board[(0,0)],self.board[(1,0)], self.board[(2,0)]], 
            [self.board[(0,0)], self.board[(0,-1)], self.board[(0,0-2)]], 
            [self.board[(0,0)], self.board[(1,-1)], self.board[(2,-2)]], 
            [self.board[(1,0)], self.board[(1,-1)], self.board[(1,-2)]],
            [self.board[(2,0)], self.board[(2,-1)], self.board[(2,-2)]],
            [self.board[(2,0)], self.board[(1,-1)], self.board[(0,-2)]]
        ]
        for winner in self.winners:
            # print(winner)
            if winner == ['x', 'x', 'x'] or winner == ['o', 'o', 'o']:#edge case is lowercase text, figure that out
                return True
            else:
                return False#maybe
    def is_full(self):
        self.spots = [self.board[(0,0)],self.board[(1,0)], self.board[(2,0)], self.board[(0,0)], self.board[(0,-1)], self.board[(0,0-2)], self.board[(0,0)], self.board[(1,-1)], self.board[(2,-2)], self.board[(1,0)], self.board[(1,-1)], self.board[(1,-2)],self.board[(2,0)], self.board[(2,-1)], self.board[(2,-2)],self.board[(2,0)], self.board[(1,-1)], self.board[(0,-2)]]
        self.list_spots = len(self.spots)
        if '-' in self.spots:
            return False
        return True
        # for spot in self.spots: #This is wrong as it only examines one element of the list at a time
        #     print(spot)
        #     if spot != '-':
        #         return True
        #     else:
        #         return False
    def is_game_over(self):
        self.winners = [
            [self.board[(0,0)],self.board[(1,0)], self.board[(2,0)]], 
            [self.board[(0,0)], self.board[(0,-1)], self.board[(0,0-2)]], 
            [self.board[(0,0)], self.board[(1,-1)], self.board[(2,-2)]], 
            [self.board[(1,0)], self.board[(1,-1)], self.board[(1,-2)]],
            [self.board[(2,0)], self.board[(2,-1)], self.board[(2,-2)]],
            [self.board[(2,0)], self.board[(1,-1)], self.board[(0,-2)]]
        ]
        self.spots = [self.board[(0,0)],self.board[(1,0)], self.board[(2,0)], self.board[(0,0)], self.board[(0,-1)], self.board[(0,0-2)], self.board[(0,0)], self.board[(1,-1)], self.board[(2,-2)], self.board[(1,0)], self.board[(1,-1)], self.board[(1,-2)],self.board[(2,0)], self.board[(2,-1)], self.board[(2,-2)],self.board[(2,0)], self.board[(1,-1)], self.board[(0,-2)]]            
        for winner in self.winners:
            print(winner)
            if winner == ['x','x','x'] or winner == ['o','o','o']:#edge case is lowercase text, figure that out
                won = True#set variable to true or false then after for loop return variable.
            elif '-' in self.spots:
                full = False
            elif '-' not in self.spots:
                full = True
        if won == True or full == True:#I think this works now...
            return True
        else:
            return False
game = Game()#new instance of game
player1 = Player('x', 'player1')
player2 = Player('o', 'player2')
#print(game.move(0,0,player))
print(game.__repr__())
print(player1.token)
print(player2.token)
print(game.move(0,0, player1.token))#displays none but does affect __repr__

print(game.move(1,0,player2.token))
print(game.move(2,0,player1.token))
print(game.move(0,-1,player1.token))
print(game.move(0,-2,player1.token))
print(game.move(1,-1,player1.token))
print(game.move(1,-2,player1.token))
#print(game.move(2,-1,player1.token))
#print(game.move(2,-2,player1.token))
print(game.__repr__)
# print(game.calc_winner())
# print(game.is_full())
print(game.is_game_over())
# print(Game())
# board_structure = [('','',''),('','',''),('','','')] #see data design OOP notebook

# for position in board_structure:
#     position.board

# print(Game.__repr__) printing the memory location