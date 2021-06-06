game_board = {"1": " ", "2": " ", "3": " ",
            "4": " ", "5": " ", "6": " ",
            "7": " ", "8": " ", "9": " "}
game_spaces = []
for space in game_board:
    game_spaces.append(space)

def board(game_board):
    print(game_board["1"] + '|' + game_board["2"] + '|' + game_board["3"])
    print(game_board["4"] + '|' + game_board["5"] + '|' + game_board["6"])
    print(game_board["7"] + '|' + game_board["8"] + '|' + game_board["9"])
def intro():
    print("Here is the game board, enter the number of the square you would like to place your token.")
    print("Player one is 'X' and player two is 'O'.")
    print("1|2|3")
    print("4|5|6")
    print("7|8|9")
    print("—————")
def gameplay():
    intro()
    player = "X"
    turn_counter = 0
    for turns in range(10):
        board(game_board)
        print(f"It's now {player}'s turn.")
        move = input()        
        if game_board[move] == " ":
            game_board[move] = player
            turn_counter += 1
        else:
            print("Space taken. Try again?")
            continue     
        if turn_counter >= 5:
            if game_board["1"] == game_board["2"] == game_board["3"] != " ":
                board(game_board)                
                print(f"Player {player} wins!")   
                break              
            elif game_board["4"] == game_board["5"] == game_board["6"] != " ":
                board(game_board)                
                print(f"Player {player} wins!") 
                break 
            elif game_board["7"] == game_board["8"] == game_board["9"] != " ":
                board(game_board)                
                print(f"Player {player} wins!") 
                break 
            elif game_board["1"] == game_board["4"] == game_board["7"] != " ":
                board(game_board)                
                print(f"Player {player} wins!") 
                break 
            elif game_board["2"] == game_board["5"] == game_board["8"] != " ":
                board(game_board)                
                print(f"Player {player} wins!") 
                break 
            elif game_board["3"] == game_board["6"] == game_board["9"] != " ":
                board(game_board)                
                print(f"Player {player} wins!") 
                break 
            elif game_board["1"] == game_board["5"] == game_board["9"] != " ":
                board(game_board)                
                print(f"Player {player} wins!") 
                break 
            elif game_board["7"] == game_board["5"] == game_board["3"] != " ":
                board(game_board)                
                print(f"Player {player} wins!") 
                break   
        board_full(turn_counter)
        if player == "X":
            player = "O"
        else:
            player = "X"
def board_full(turn_counter):
    if turn_counter == 9:               
        print("It's a Tie!")
        quit()   
def game():
    gameplay()
    
game()

