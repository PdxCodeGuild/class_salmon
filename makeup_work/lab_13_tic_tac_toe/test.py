class Player:

    print("Start Player Class")
    def __init__(self, name, token):
        self.name = name
        self.token = token
    
    def __str__(self):
        return self.token


class Game:
    print("Start Game Class")

    # Board index locations
    def __init__(self):
        self.board = {
            "0": "0", "1": "1", "2": "2", 
            "3": "3", "4": "4", "5": "5",
            "6": "6", "7": "7", "8": "8"
            }

    # Board display
    def __repr__(self):
        return f"""
        \t{self.board["0"]}|{self.board["1"]}|{self.board["2"]}
        \t{self.board["3"]}|{self.board["4"]}|{self.board["5"]}
        \t{self.board["6"]}|{self.board["7"]}|{self.board["8"]}
        """

    def move(self, index, token ):
        print("Im Move")
        self.index = index
        self.token = token

        print(self.index)
        print(self.token)
        print(self.board)


        move = { self.index: self.token}
        print(self.board.update(move))


        

# import datetime
# dt = datetime.datetime.now()
# print(dt)
# print(str(dt))
# print(repr(dt))
# print(dt.__repr__())
# dt2 = eval(repr(dt)) # a way to clone an object


class Point:
    def __init__(self, a, b):
        self.x = a
        self.y = b
    
    def __str__(self):
        return f'(hi {self.x},{self.y})'

p = Point(5, 2)
print(p.x) # 5
print(p)
# s = str(p)
# print(s)
# print(p.__str__())
# print(Point.__str__(p))






def main():
    print("Start Main Class")
    # Player REPL 

    user1 = Player(input("Whoever wants to be 'x', enter a name: "), "x")
    user2 = Player(input("Whoever wants to be 'o', enter a name: "), "o")

    print(f"\nVery Well, {user1.name} is playing as {user1.token}, and {user2.name} is stuck as {user2.token}.\nLet's start this...")

    board = Game()
    print(board)
    print(board.move("0", user1.token))


  




    
    

# if __name__ == "__main__":
#     main()