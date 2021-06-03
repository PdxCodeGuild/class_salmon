# represent the board with a dictionary with keys from 1-9 that reflect blank, X, or O
game_board = {
    '0,0': "b",
    '0,1': "b",
    '0,2': "b",
    '1,0': "b",
    '1,1': "b",
    '1,2': "b",
    '2,0': "b",
    '2,1': "b",
    '2,2': "b",
}


class Player:
    def __init__(self, x_or_o):
        self.select = x_or_o




'''    def select(self, player_num):
        self.select = player_num
        if self.select == 'X':
            return 'X'
        elif self.select == '2':
            return 'O'''

class Game:
    def __init__(self):
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
        return self.visual(self.game_board)

    def visual(self, game_board):
        visual_list = []
        for i in self.game_board:
            visual_list.append(self.game_board[i])
        visual_str = '|'.join(visual_list)
        # print(visual_list)
        # print(visual_str)
        self.line_one = visual_str[0:5]
        self.line_two = visual_str[6:11]
        self.line_three = visual_str[12:17]
        return self.line_one + "\n" + self.line_two + "\n" + self.line_three

    def move(self, x, y, player):
        self.game_board[f"{x},{y}"] = player
        # print(self.game_board)
        return self.visual(game_board)

# return true or False to end the while loop to end the game in victory or defeat
    def calc_winner(self):
        '''print(self.line_one + str(self.line_one.count('X')))
        print(self.line_two + str(self.line_two.count('X')))
        print(self.line_three + str(self.line_three.count('X')))'''
        if self.line_one.count('X') == 3:
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
        elif self.line_one[0] == 'X' and self.line_two[2] == 'X' and self.line_three[4] == 'X':
            return True
        elif self.line_one[0] == 'O' and self.line_two[2] == 'O' and self.line_three[4] == 'O':
            return True
        elif self.line_one[4] == 'X' and self.line_two[2] == 'X' and self.line_three[0] == 'X':
            return True
        elif self.line_one[4] == 'O' and self.line_two[2] == 'O' and self.line_three[0] == 'O':
            return True
        else:
            False
        
    def is_full(self):
        for i in self.game_board:
            if game_board[i] == " ":
                return False
            else:
                return True
'''
    def is_game_over(self):'''
    

def main():
    print("Let's play a game.")
    print("Please choose X or O and a grid location to make your move when prompted.")
    print("Grid locations will use an X,Y format. So to place a mark in the top left portion of the grid, you'd enter '0,0'. If in the middle, '1,1'.")
    x_or_o = input("But first, are you player one ('X') or player two ('O')? ").upper()
    player = Player(x_or_o)
    game = Game()
    print(f"Okay, you will be using {x_or_o}'s to mark your moves. ")
    while True:
        print(f"Here is the board:\n{game.__repr__()}")
        x = input(f"Please enter the x-coordinate for your move: ")
        y = input(f"Please enter the y-coordinate for your move: ")
        game.move(x, y, x_or_o)
        if game.calc_winner():
            print(f"The game is over. Congratulations to the winner.")
            print(f"Here is the final board:\n{game.__repr__()}")
            # Update this later to congratulate whoever won (X or O)
            break
        if game.is_full():
            print("The board is full. The game has ended in a draw. Thanks for playing.")
       # Print the board after each turn, including the computer's move

main()
