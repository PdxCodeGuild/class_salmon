import click
# Create a player class
# Player class will have properties associated with a player
# - name -> name of the player
# - token -> is the player 'x' or 'o'
# - moves -> list that contains the moves that the player has made

class Player:

    def __init__(self, name, token, score):
        self.name = name
        self.token = token
        self.score = 0

    def __str__(self):
        return self.token

#******************************************************#
# ***** TEST PLAYER CLASS *****

# p1 = Player(input("Whoever wants to be 'x', enter a name: "), "x", None)
# p2 = Player(input("Whoever wants to be 'o', enter a name: "), "o", None)

# print(f"Name: {p1.name}\nToken: {p1.token}\nMoves: {p1.moves}")

# # Name: p1
# # Token: x
# # Moves: []

# p1 = Player("p1", "x")
# p2 = Player("p2", "o")

p1score = 0
p2score = 0

#******************************************************#




# Create a game class
# Game class will have properties associated with a tic-tac-toe board
# - board -> dictionary with numbers representing the grid layout 
# - __str__ -> displays the board. takes in dict key and updates values with tokens
# - calc_winner -> checks the players move list to see if there is a combination of winning positions.
# - move -> takes in the dict key and updates the value with the token. adds the dict key to the players list.
# - is_full -> checks there are any remaining positions on the board 

class Game:

    def __init__(self):
        self.board = {
            "1": 1,"2": 2,"3": 3,
            "4": 4,"5": 5,"6": 6,
            "7": 7,"8": 8,"9": 9,
        }

    def __str__(self):
        return f"""
        \t{self.board["6"]}|{self.board["1"]}|{self.board["8"]}
        \t{self.board["7"]}|{self.board["5"]}|{self.board["3"]}
        \t{self.board["2"]}|{self.board["9"]}|{self.board["4"]}
        """

    def move(self, key, value):
        # Update the board position with the player token
        self.board[key] = value
        self.board.update({f"{key}": value})

        # # Add the move to the players move list
        # print(f"score {key}")
        # return p1score + key if value != "o" else p2score + key

    def calc_winner(self, score, name):
        if score == 15:
            
            return True
        
    def is_full(self, p1score, p2score):
        return True if (p1score + p2score) == 45 else False

    def is_game_over():
        # return True if Game.calc_winner() or Game.is_full() else False
        pass

        

#******************************************************#
# ***** TEST GAME CLASS *****

# board = Game()
# print(board)
# 0|1|2
# 3|4|5
# 6|7|8
 
# print(board.move(int(1), "x"))
# print(board.move(int(2), "o"))
# print(board)
# x|1|o
# 6|4|5
# 6|7|8

# print(f"player score: {p1score}")
# [0]

# print(board.calc_winner(15,"player1"))
# print(board.is_full(24,20))

#******************************************************#

def clrscr():
   # Clear screen using click.clear() function
    click.clear()

    print(49 * "*")
    print(18 * "-" + " TIC-TAC-TOE " + 18 * "-")
    print(49 * "*")

# Create a Main function to model the gameplay

def main():
    clrscr()
    # Player REPL 
    # - Take in player names and create a player class
    # - Start the board
    p1 = Player(input("Whoever wants to be 'x', enter a name: "), "x", 0)
    p2 = Player(input("Whoever wants to be 'o', enter a name: "), "o", 0)

    print(f"\nVery Well, {p1.name} is playing as {p1.token}, and {p2.name} is stuck as {p2.token}.\nLet's start this...")

    board = Game()


    # Begin the while loop
    turn_counter = 0
    while turn_counter != 9:
        clrscr()
        print(board)
        players = [p1, p2]
        player = players[turn_counter % len(players)]
        print(player.score)

        move_prompt = int(input(f"\n{player.name}'s turn.\nEnter the number where you would like to place an {player.token}: "))
        board.move(move_prompt, player.token)
        player.score += move_prompt

        if board.calc_winner(player.score,player.name):
            print(f"{player.name} wins.")
            break



        turn_counter += 1


play_again = 'y'
while play_again == 'y':
    main()
    play_again = input('Game Over. Play again? (y/n): ')
  
# if __name__ == "__main__":
#     main()



#******************************************************#



#******************************************************#