import random

class Player:
    def __init__(self, x_or_o):
        self.select = x_or_o

    def computer_select(self):
        return 'X' if self.select == "O" else 'O'

    def player_two(self):
        return 'X' if self.select == "O" else 'O'

class Game:
    def __init__(self):
    # represent the board with a dictionary with keys from 1-9 that reflect blank, X, or O
        self.game_board = {
            '0,0': " ",
            '0,1': " ",
            '0,2': " ",
            '1,0': " ",
            '1,1': " ",
            '1,2': " ",
            '2,0': " ",
            '2,1': " ",
            '2,2': " ",
        }

    def __repr__(self):
        self.visual_list = []
        for i in self.game_board:
            self.visual_list.append(self.game_board[i])
        self.visual_str = '|'.join(self.visual_list)
        # print(visual_list)
        # print(visual_str)
        self.line_one = self.visual_str[0:5]
        self.line_two = self.visual_str[6:11]
        self.line_three = self.visual_str[12:17]
        return self.line_one + "\n" + self.line_two + "\n" + self.line_three

    def move(self, x, y, player):
        if self.acceptable_move(x, y) == False:
            print(f"Sorry you cannot place your {player} there.")
        elif self.acceptable_move(x, y) == True:
            self.game_board[f"{x},{y}"] = player
        # print(self.game_board)
        return self.__repr__()

    def acceptable_move(self, x, y):
        try:
            if self.game_board[f'{x},{y}'] == ' ':
                return True
            else:
                return False
        except KeyError():
                return False

# return true or False to end the while loop to end the game in victory or defeat
    def calc_winner(self):
        '''print(self.line_one + str(self.line_one.count('X')))
        print(self.line_two + str(self.line_two.count('X')))
        print(self.line_three + str(self.line_three.count('X')))'''
        if self.line_one.count('X') == 3: # this and the following 5 elifs check for a horizontal win
            return True
        elif self.line_two.count('X') == 3:
            return True
        elif self.line_three.count('X') == 3:
            return True
        elif self.line_one.count('O') == 3:
            return True
        elif self.line_two.count('O') == 3:
            return True
        elif self.line_three.count('O') == 3:
            return True
        elif self.line_one[0] == 'X' and self.line_two[2] == 'X' and self.line_three[4] == 'X': # this and the following 3 elifs check for a diagonal win
            return True
        elif self.line_one[0] == 'O' and self.line_two[2] == 'O' and self.line_three[4] == 'O':
            return True
        elif self.line_one[4] == 'X' and self.line_two[2] == 'X' and self.line_three[0] == 'X':
            return True
        elif self.line_one[4] == 'O' and self.line_two[2] == 'O' and self.line_three[0] == 'O':
            return True
        elif self.line_one[0] == 'O' and self.line_two[0] == 'O' and self.line_three[0] == 'O': # this and the remaining elifs check for vertical wins
            return True
        elif self.line_one[2] == 'O' and self.line_two[2] == 'O' and self.line_three[2] == 'O':
            return True
        elif self.line_one[4] == 'O' and self.line_two[4] == 'O' and self.line_three[4] == 'O':
            return True
        elif self.line_one[0] == 'X' and self.line_two[0] == 'X' and self.line_three[0] == 'X':
            return True
        elif self.line_one[2] == 'X' and self.line_two[2] == 'X' and self.line_three[2] == 'X':
            return True
        elif self.line_one[4] == 'X' and self.line_two[4] == 'X' and self.line_three[4] == 'X':
            return True
        else:
            False
        
    def is_full(self):
        # print(self.game_board)
        for i in self.game_board:
            if self.game_board[i] == " ":
                return False
            else:
                pass
        print("The board is full. The game has ended in a draw. Thanks for playing.")
        return True

    def is_game_over(self):
        if self.is_full():
            print("The game is over.")
            return True
        elif self.calc_winner():
            print("The game is over.")
            return True
        else:
            return False

def one_player():
    x_or_o = input("\nWill you play as ('X') or ('O')?  ").upper()
    player = Player(x_or_o)
    computer = player.computer_select()
    print("Since you chose " + x_or_o + ", the Computer is " + computer + "'s\n")
    game = Game()
    while True:
        x = input(f"Please enter the x-coordinate for your move: ")
        y = input(f"Please enter the y-coordinate for your move: ")
        game.move(x, y, x_or_o)
        print(f"Here is the board after your move:\n{game.__repr__()}")
        if game.calc_winner():
            print(f"The game is over. Congratulations to the {x_or_o} player.")
            break
        if game.is_full():
            break
        if game.is_game_over():
            break
        print(f"\nNow it's the computer's turn.\n")
        game.move(random.randint(0, 2), random.randint(0, 2), computer)
        print(f"\nHere is the board after the computer's move:\n{game.__repr__()}")
        if game.calc_winner():
            print(f"The game is over. Congratulations to the {computer} player.")
            break
        if game.is_full():
            break
        if game.is_game_over():
            break
       # Print the board after each turn, including the computer's move

def main():
    x_or_o = input("\nWill you play as ('X') or ('O')? ").upper()
    player = Player(x_or_o)
    player_two = player.player_two()
    print("Player one chose " + x_or_o + ", so Player two is " + player_two + "'s\n")
    game = Game()
    while True:
        x = input(f"Please enter the x-coordinate for your move: ")
        y = input(f"Please enter the y-coordinate for your move: ")
        game.move(x, y, x_or_o)
        print(f"Here is the board after your move:\n{game.__repr__()}")
        if game.calc_winner():
            print(f"The game is over. Congratulations to the {x_or_o} player.")
            break
        if game.is_full():
            break
        if game.is_game_over():
            break
        print(f"\nNow it's player two's turn.\n")
        x = input(f"Please enter the x-coordinate for your move: ")
        y = input(f"Please enter the y-coordinate for your move: ")
        game.move(x, y, player_two)
        print(f"\nHere is the board after player two's move:\n{game.__repr__()}")
        if game.calc_winner():
            print(f"The game is over. Congratulations to the {computer} player.")
            break
        if game.is_full():
            break
        if game.is_game_over():
            break

print("Let's play a game.")
print("Please choose X or O and a grid location to make your move when prompted.")
print("Grid locations will use an X,Y format. \nTo place a mark in the top left portion of the grid, you'll enter '0,0'. If in the middle, '1,1'.")
p1_or_p2 = input("Do you want to play against the computer (1) or against another person (2)? ")
if p1_or_p2 == "1":
    one_player()
elif p1_or_p2 == "2":
    main()