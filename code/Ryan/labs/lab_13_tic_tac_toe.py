# --------------------------------------------------------------------------------------#

#  Script logic
# 1) make a 3x3 board where every box has a unique value (index number)
# 2) make a list of all possible locations on the board
# 3) make a running list for x and o positions
# 4) alternate turns for x and o placement, taking in input from user, and assigning x or o to the position
# 5) display the updated board at the start of each turn
# 6) each time user chooses a position, remove that from the possibilities list and add it to the x or o list
# 7) starting at turn 5, go through the x or o list and check if there is a winning combination of numbers
# 8) if there is a winning combination, declare the winner and end game
# 9) at the end if there is no winners, the game is a draw and ends

# TODO duplicate entries break out of script fully instead of asking for another input
# TODO board.is_game_over() / play_game starts off as True instead of False

# --------------------------------------------------------------------------------------#
import os
import sys

def main(user_inputs):
    pass


class Game:
    def __init__(self): # this is the initializer
        self.board = {"0": "0","1": "1","2": "2","3": "3","4": "4","5": "5","6": "6","7": "7","8": "8"} # these are member variables
        #self.continue = True
        self.x_list = []
        self.o_list = []
    # Function to print Tic Tac Toe
    def __repr__(self):
        return f"""\t{self.board['0']}|{self.board['1']}|{self.board['2']}
  \t{self.board['3']}|{self.board['4']}|{self.board['5']}
  \t{self.board['6']}|{self.board['7']}|{self.board['8']}"""


    # Write move(x, y, player) Place a player's token character string at a given coordinate (top-left is 0, 0), 
    # x is horizontal position, y is vertical position.

    def move(self, input, player):
        self.board[input] = player.token
        #self.counter += 1
        # if player.token == "x":
        #     x_list += input
            
        # elif player.token == "o":
        #     self.o_list += input

    def calc_winner(self, player_name):
        self.player_name = player_name
        return self.player_name + "Wins"

    def is_full(self):
        pass

    def is_game_over(self):
        pass



class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token

player1 = Player("player1","x")
player2 = Player("player2","o")

#print(player1.name)
#print(player1.token)

game = Game()
# print(type(game))
# print(type(game.board))
# print(type(game.move))
# game.move("0",player1)
# game.board["1"] = player2.token
#print(game.x_list)
#print(game.o_list)
print(game)

# Running list for x and o positions
x = []
o = []

# All possible locations on board
possible_positions = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]

#while game.continue == True:

play_game = True
while play_game:
# x Turn 1
    player1_input = input("player x choose a number: ")
    if str(player1_input) not in possible_positions:
        print("Position not available. Please try again")
        continue
    else:
        game.move(player1_input, player1)
        x.append(player1_input)
        #print(x)
        possible_positions.remove(player1_input)
        print(game)

# o Turn 2
        player2_input = input("player o choose a number: ")
        if str(player2_input) not in possible_positions:
            print("Position not available. Please play again")
            play_game = False 
        else:
            game.move(player2_input, player2)
            o.append(player2_input)
            #print(o)
            possible_positions.remove(player2_input)
            print(game)

# x Turn 3
            player1_input = input("player x choose a number: ")
            if str(player1_input) not in possible_positions:
                print("Position not available. Please play again")
                play_game = False
            else:
                game.move(player1_input, player1)
                x.append(player1_input)
                #print(x)
                possible_positions.remove(player1_input)
                print(game)

# o Turn 4
                player2_input = input("player o choose a number: ")
                if str(player2_input) not in possible_positions:
                    print("Position not available. Please play again")
                    play_game = False 
                else:
                    game.move(player2_input, player2)
                    o.append(player2_input)
                    #print(o)
                    possible_positions.remove(player2_input)
                    print(game)

# x Turn 5 (x win starts)
                    player1_input = input("player x choose a number: ")
                    if str(player1_input) not in possible_positions:
                        print("Position not available. Please play again")
                        play_game = False
                    else:
                        game.move(player1_input, player1)
                        x.append(player1_input)
                        #print(x)
                        # Check for winning combination in x list
                        if ('0' in x and '1' in x and '2' in x) or ('3' in x and '4' in x and '5' in x) or ('6' in x and '7' in x and '8' in x) or ('0' in x and '3' in x and '6' in x) or ('1' in x and '4' in x and '7' in x) or ('2' in x and '5' in x and '8' in x) or ('0' in x and '4' in x and '8' in x) or ('2' in x and '4' in x and '6' in x):
                            game.player_name = "x"
                            print(f"{game.player_name} wins")
                            print(game)
                            break
                        possible_positions.remove(player1_input)
                        print(game)
# o Turn 6 (o win starts)
                        player2_input = input("player o choose a number: ")
                        if str(player2_input) not in possible_positions:
                            print("Position not available. Please play again")
                            play_game = False 
                        else:
                            game.move(player2_input, player2)
                            o.append(player2_input)
                            #print(o)
                            # Check for winning combination in o list
                            if ('0' in o and '1' in o and '2' in o) or ('3' in o and '4' in o and '5' in o) or ('6' in o and '7' in o and '8' in o) or ('0' in o and '3' in o and '6' in o) or ('1' in o and '4' in o and '7' in o) or ('2' in o and '5' in o and '8' in o) or ('0' in o and '4' in o and '8' in o) or ('2' in o and '4' in o and '6' in o):
                                game.player_name = "o"
                                print(f"{game.player_name} wins")
                                print(game)
                                break
                            possible_positions.remove(player2_input)
                            print(game)
# x Turn 7
                            player1_input = input("player x choose a number: ")
                            if str(player1_input) not in possible_positions:
                                print("Position not available. Please play again")
                                play_game = False
                            else:
                                game.move(player1_input, player1)
                                x.append(player1_input)
                                #print(x)
                                # Check for winning combination in x list
                                if ('0' in x and '1' in x and '2' in x) or ('3' in x and '4' in x and '5' in x) or ('6' in x and '7' in x and '8' in x) or ('0' in x and '3' in x and '6' in x) or ('1' in x and '4' in x and '7' in x) or ('2' in x and '5' in x and '8' in x) or ('0' in x and '4' in x and '8' in x) or ('2' in x and '4' in x and '6' in x):
                                    game.player_name = "x"
                                    print(f"{game.player_name} wins")
                                    print(game)
                                    break
                                possible_positions.remove(player1_input)
                                print(game)
# o Turn 8
                                player2_input = input("player o choose a number: ")
                                if str(player2_input) not in possible_positions:
                                    print("Position not available. Please play again")
                                    play_game = False 
                                else:
                                    game.move(player2_input, player2)
                                    o.append(player2_input)
                                    #print(o)
                                    # Check for winning combination in o list
                                    if ('0' in o and '1' in o and '2' in o) or ('3' in o and '4' in o and '5' in o) or ('6' in o and '7' in o and '8' in o) or ('0' in o and '3' in o and '6' in o) or ('1' in o and '4' in o and '7' in o) or ('2' in o and '5' in o and '8' in o) or ('0' in o and '4' in o and '8' in o) or ('2' in o and '4' in o and '6' in o):
                                        game.player_name = "o"
                                        print(f"{game.player_name} wins")
                                        print(game)
                                        break
                                    possible_positions.remove(player2_input)
                                    print(game)
                                    
# x Turn 9
                                    player1_input = input("player x choose a number: ")
                                    if str(player1_input) not in possible_positions:
                                        print("Position not available. Please play again")
                                        play_game = False
                                    else:
                                        game.move(player1_input, player1)
                                        x.append(player1_input)
                                        #print(x)
                                        # Check for winning combination in x list
                                        if ('0' in x and '1' in x and '2' in x) or ('3' in x and '4' in x and '5' in x) or ('6' in x and '7' in x and '8' in x) or ('0' in x and '3' in x and '6' in x) or ('1' in x and '4' in x and '7' in x) or ('2' in x and '5' in x and '8' in x) or ('0' in x and '4' in x and '8' in x) or ('2' in x and '4' in x and '6' in x):
                                            game.player_name = "x"
                                            print(f"{game.player_name} wins")
                                            print(game)
                                            break
                                        possible_positions.remove(player1_input)
                                        print(game)
                                        

# Game ends here
                                        print("Board full. Draw.")
                                        sys.stdout.flush()
                                        os.execv(sys.argv[0], sys.argv)
                                        #play_again = input("Play again? (y/n): ")
                                        #if play_again != "y":
                                        #    play_game = False

#----------------------------------------------------------------------------------#
# # make 2 lists, one for x and one for o
# # alternate filling the lists
# # when the count of the lists added together is 9
# # sort each list
# # if the list matches any of the winning combinations
# # declare the winner

# x = []
# o = []

# #print(type(x))
# #total_list_size = len(x) + len(o)

# #print(type(total_list_size))
# #print(total_list_size)

# possible_positions = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]

# board_dict = {
#     "0": "",
#     "1": "",
#     "2": "",
#     "3": "",
#     "4": "",
#     "5": "",
#     "6": "",
#     "7": "",
#     "8": "",
#     }


# board =f"""
# \t{board_dict["0"]}|{board_dict["1"]}|{board_dict["2"]}
# \t{board_dict["3"]}|{board_dict["4"]}|{board_dict["5"]}
# \t{board_dict["6"]}|{board_dict["7"]}|{board_dict["8"]}
# """

# while len(x) + len(o) < 9:
#     board =f"""
# \t{board_dict["0"]}|{board_dict["1"]}|{board_dict["2"]}
# \t{board_dict["3"]}|{board_dict["4"]}|{board_dict["5"]}
# \t{board_dict["6"]}|{board_dict["7"]}|{board_dict["8"]}
#     """
#     print(f"Possible choices {possible_positions}")
#     turn_1 = input("Pick spot to enter a x: ")
#     if str(turn_1) not in possible_positions:
#         print("Position not available. Please try again")
#         continue
#     else:
#         x.append(turn_1)
#         print(turn_1)
#         print(type(turn_1))
#         board_dict[turn_1] = "x"
#         board =f"""
#         \t{board_dict.get(turn_1)}|{board_dict["1"]}|{board_dict["2"]}
#         \t{board_dict["3"]}|{board_dict["4"]}|{board_dict["5"]}
#         \t{board_dict["6"]}|{board_dict["7"]}|{board_dict["8"]}
#         """
#         possible_positions.remove(turn_1)

#         print(f"Possible choices {possible_positions}")
#         print(board)
#         turn_2 = input("Pick spot to enter a o: ")
#         if str(turn_2) not in possible_positions:
#             print("Position not available. Please try again")
#             continue
#         else:
#             o.append(turn_2)
#             possible_positions.remove(turn_2)

#             print(f"Possible choices {possible_positions}")
#             turn_3 = input("Pick spot to enter a x: ")
#             if str(turn_3) not in possible_positions:
#                 print("Position not available. Please try again")
#                 continue
#             else:
#                 x.append(turn_3)
#                 possible_positions.remove(turn_3)

#                 print(f"Possible choices {possible_positions}")
#                 turn_4 = input("Pick spot to enter a o: ")
#                 if str(turn_4) not in possible_positions:
#                     print("Position not available. Please try again")
#                     continue
#                 else:
#                     o.append(turn_4)
#                     possible_positions.remove(turn_4)

#                     print(f"Possible choices {possible_positions}")
#                     turn_5 = input("Pick spot to enter a x: ")
#                     if str(turn_5) not in possible_positions:
#                         print("Position not available. Please try again")
#                         continue
#                     else:
#                         x.append(turn_5)
#                             # Check for winning combination in x list
#                             # row wins
#                         if ('0' in x and '1' in x and '2' in x) or ('3' in x and '4' in x and '5' in x) or ('6' in x and '7' in x and '8' in x):
#                             print(f"x wins")
#                             break

#                         # column wins
#                         elif ('0' in x and '3' in x and '6' in x) or ('1' in x and '4' in x and '7' in x) or ('2' in x and '5' in x and '8' in x):
#                             print(f"x wins")
#                             break

#                         # cross wins
#                         elif ('0' in x and '4' in x and '8' in x) or ('2' in x and '4' in x and '6' in x):
#                             print(f"x wins")
#                             break

#                         possible_positions.remove(turn_5)

#                         print(f"Possible choices {possible_positions}")
#                         turn_6 = input("Pick spot to enter a o: ")
#                         if str(turn_6) not in possible_positions:
#                             print("Position not available. Please try again")
#                             continue
#                         else:
#                             o.append(turn_6)
#                             # Check for winning combination in o list
#                                 # row wins
#                             if ('0' in o and '1' in o and '2' in o) or ('3' in o and '4' in o and '5' in o) or ('6' in o and '7' in o and '8' in o):
#                                 print(f"o wins")
#                                 break

#                             # column wins
#                             elif ('0' in o and '3' in o and '6' in o) or ('1' in o and '4' in o and '7' in o) or ('2' in o and '5' in o and '8' in o):
#                                 print(f"o wins")
#                                 break

#                             # cross wins
#                             elif ('0' in o and '4' in o and '8' in o) or ('2' in o and '4' in o and '6' in o):
#                                 print(f"o wins")
#                                 break

#                             possible_positions.remove(turn_6)

#                             print(f"Possible choices {possible_positions}")
#                             turn_7 = input("Pick spot to enter a x: ")
#                             if str(turn_7) not in possible_positions:
#                                 print("Position not available. Please try again")
#                                 continue
#                             else:
#                                 x.append(turn_7)
#                             # Check for winning combination in x list
#                             # row wins
#                                 if ('0' in x and '1' in x and '2' in x) or ('3' in x and '4' in x and '5' in x) or ('6' in x and '7' in x and '8' in x):
#                                     print(f"x wins")
#                                     break

#                                 # column wins
#                                 elif ('0' in x and '3' in x and '6' in x) or ('1' in x and '4' in x and '7' in x) or ('2' in x and '5' in x and '8' in x):
#                                     print(f"x wins")
#                                     break

#                                 # cross wins
#                                 elif ('0' in x and '4' in x and '8' in x) or ('2' in x and '4' in x and '6' in x):
#                                     print(f"x wins")
#                                     break

#                                 possible_positions.remove(turn_7)

#                                 print(f"Possible choices {possible_positions}")
#                                 turn_8 = input("Pick spot to enter a o: ")
#                                 if str(turn_8) not in possible_positions:
#                                     print("Position not available. Please try again")
#                                     continue
#                                 else:
#                                     o.append(turn_8)
#                                     # Check for winning combination in o list
#                                         # row wins
#                                     if ('0' in o and '1' in o and '2' in o) or ('3' in o and '4' in o and '5' in o) or ('6' in o and '7' in o and '8' in o):
#                                         print(f"o wins")
#                                         break

#                                     # column wins
#                                     elif ('0' in o and '3' in o and '6' in o) or ('1' in o and '4' in o and '7' in o) or ('2' in o and '5' in o and '8' in o):
#                                         print(f"o wins")
#                                         break

#                                     # cross wins
#                                     elif ('0' in o and '4' in o and '8' in o) or ('2' in o and '4' in o and '6' in o):
#                                         print(f"o wins")
#                                         break

#                                     possible_positions.remove(turn_8)

#                                     print(f"Possible choices {possible_positions}")
#                                     turn_9 = input("Pick spot to enter a x: ")
#                                     if str(turn_9) not in possible_positions:
#                                         print("Position not available. Please try again")
#                                         continue
#                                     else:
#                                         x.append(turn_9)
#                                             # Check for winning combination in x list
#                                             # row wins
#                                         if ('0' in x and '1' in x and '2' in x) or ('3' in x and '4' in x and '5' in x) or ('6' in x and '7' in x and '8' in x):
#                                             print(f"x wins")
#                                             break

#                                         # column wins
#                                         elif ('0' in x and '3' in x and '6' in x) or ('1' in x and '4' in x and '7' in x) or ('2' in x and '5' in x and '8' in x):
#                                             print(f"x wins")
#                                             break

#                                         # cross wins
#                                         elif ('0' in x and '4' in x and '8' in x) or ('2' in x and '4' in x and '6' in x):
#                                             print(f"x wins")
#                                             break

#                                         possible_positions.remove(turn_9)

#     x.sort()
#     o.sort()
#     print(x)
#     print(o)

#     # # Check for winning combination in x list
#     #     # row wins
#     # if ('0' in x and '1' in x and '2' in x) or ('3' in x and '4' in x and '5' in x) or ('6' in x and '7' in x and '8' in x):
#     #     print(f"x wins")

#     # # column wins
#     # elif ('0' in x and '3' in x and '6' in x) or ('1' in x and '4' in x and '7' in x) or ('2' in x and '5' in x and '8' in x):
#     #     print(f"x wins")

#     # # cross wins
#     # elif ('0' in x and '4' in x and '8' in x) or ('2' in x and '4' in x and '6' in x):
#     #     print(f"x wins")


#     # # Check for winning combination in o list
#     #     # row wins
#     # if ('0' in o and '1' in o and '2' in o) or ('3' in o and '4' in o and '5' in o) or ('6' in o and '7' in o and '8' in o):
#     #     print(f"o wins")

#     # # column wins
#     # elif ('0' in o and '3' in o and '6' in o) or ('1' in o and '4' in o and '7' in o) or ('2' in o and '5' in o and '8' in o):
#     #     print(f"o wins")

#     # # cross wins
#     # elif ('0' in o and '4' in o and '8' in o) or ('2' in o and '4' in o and '6' in o):
#     #     print(f"o wins")


# # -------------------------------Brute force combinations-------------------------------------------#

# # # Show board with coordinates
# # # Which player turn is it?
# # # Pick coordinate of the board
# # # If statement to add to board
# # # Add the letter to the board
# # # Change to other player

# # firstfirst_player = ""

# # pick_player = input("Whose turn? (x or o): ")

# # if pick_player != "x":
# #     first_player = "o"
# # else:
# #     first_player = pick_player

# # print(f"Current Player: {first_player}")

# # board = f"""

# # \t  a|b|c

# # \t1) | | 
# # \t2) | |
# # \t3) | |

# # """

# # print(board)

# # first_move = input("Pick a coordinate: ")

# # if first_move == "a1":
# #     board = f"""

# #     \t  a|b|c

# #     \t1){first_player}| | 
# #     \t2) | |
# #     \t3) | |

# #     """
# # elif first_move == "a2":
# #     board = f"""

# #     \t  a|b|c

# #     \t1) |{first_player}| 
# #     \t2) | |
# #     \t3) | |

# #     """
# # elif first_move == "a3":
# #     board = f"""

# #     \t  a|b|c

# #     \t1) ||{first_player}
# #     \t2) | |
# #     \t3) | |

# #     """
# # elif first_move == "b1":
# #     board = f"""

# #     \t  a|b|c

# #     \t1) || 
# #     \t2){first_player}| |
# #     \t3) | |

# #     """
# # elif first_move == "b2":
# #     board = f"""

# #     \t  a|b|c

# #     \t1) || 
# #     \t2) |{first_player}|
# #     \t3) | |

# #     """
# # elif first_move == "b3":
# #     board = f"""

# #     \t  a|b|c

# #     \t1) || 
# #     \t2) | |{first_player}
# #     \t3) | |

# #     """
# # elif first_move == "c1":
# #     board = f"""

# #     \t  a|b|c

# #     \t1) || 
# #     \t2) | |
# #     \t3){first_player}| |

# #     """
# # elif first_move == "c2":
# #     board = f"""

# #     \t  a|b|c

# #     \t1) || 
# #     \t2) | |
# #     \t3) |{first_player}|

# #     """
# # elif first_move == "c3":
# #     board = f"""

# #     \t  a|b|c

# #     \t1) || 
# #     \t2) | |
# #     \t3) | |{first_player}

# #     """
# # else:
# #     "Position doesn't exist"
# # print(board)

# # # Turn 2
# # current_board = board

# # second_player = ""

# # pick_player = input("Whose turn? (x or o): ")

# # if pick_player != "x":
# #     second_player = "o"
# # else:
# #     second_player = pick_player

# # print(f"Current Player: {second_player}")

# # print(current_board)

# # second_move = input("Pick a coordinate: ")

# # # If turn 1 in a1
# # if first_move == "a1" and second_move == "a2":
# #     board = f"""

# #     \t  a|b|c

# #     \t1){first_player}|{second_player}| 
# #     \t2) | |
# #     \t3) | |

# #     """
# # elif first_move == "a1" and second_move == "a3":
# #     board = f"""

# #     \t  a|b|c

# #     \t1){first_player}||{second_player}
# #     \t2) | |
# #     \t3) | |

# #     """   
# # elif first_move == "a1" and second_move == "b1":
# #     board = f"""

# #     \t  a|b|c

# #     \t1){first_player}| |
# #     \t2){second_player}| |
# #     \t3) | |

# #     """   
# # elif first_move == "a1" and  second_move == "b2":
# #     board = f"""

# #     \t  a|b|c

# #     \t1){first_player}| |
# #     \t2) |{second_player}|
# #     \t3) | |

# #     """   
# # elif first_move == "a1" and second_move == "b3":
# #     board = f"""

# #     \t  a|b|c

# #     \t1){first_player}| |
# #     \t2) | |{second_player}
# #     \t3) | |

# #     """
# # elif first_move == "a1" and second_move == "c1":
# #     board = f"""

# #     \t  a|b|c

# #     \t1){first_player}| |
# #     \t2) | |
# #     \t3){second_player}| |

# #     """
# # elif first_move == "a1" and second_move == "c2":
# #     board = f"""

# #     \t  a|b|c

# #     \t1){first_player}| |
# #     \t2) | |
# #     \t3) |{second_player}|

# #     """
# # elif first_move == "a1" and second_move == "c3":
# #     board = f"""

# #     \t  a|b|c

# #     \t1){first_player}| |
# #     \t2) | |
# #     \t3) | |{second_player}

# #     """
# # # If turn 1 in a2
# # elif first_move == "a2" and second_move == "a1":
# #     board = f"""

# #     \t  a|b|c

# #     \t1){second_player}|{first_player}|
# #     \t2) | |
# #     \t3) | |

# #     """
# # elif first_move == "a2" and second_move == "a3":
# #     board = f"""

# #     \t  a|b|c

# #     \t1) |{first_player}|{second_player}
# #     \t2) | |
# #     \t3) | |

# #     """
# # elif first_move == "a2" and second_move == "b1":
# #     board = f"""

# #     \t  a|b|c

# #     \t1) |{first_player}|
# #     \t2){second_player}| |
# #     \t3) | |

# #     """
# # elif first_move == "a2" and second_move == "b2":
# #     board = f"""

# #     \t  a|b|c

# #     \t1) |{first_player}|
# #     \t2) |{second_player}|
# #     \t3) | |

# #     """
# # elif first_move == "a2" and second_move == "b3":
# #     board = f"""

# #     \t  a|b|c

# #     \t1) |{first_player}|
# #     \t2) | |{second_player}
# #     \t3) | |

# #     """
# # elif first_move == "a2" and second_move == "c1":
# #     board = f"""

# #     \t  a|b|c

# #     \t1) |{first_player}|
# #     \t2) | |
# #     \t3){second_player}| |

# #     """
# # elif first_move == "a2" and second_move == "c2":
# #     board = f"""

# #     \t  a|b|c

# #     \t1) |{first_player}|
# #     \t2) | |
# #     \t3) |{second_player}|

# #     """
# # elif first_move == "a2" and second_move == "c3":
# #     board = f"""

# #     \t  a|b|c

# #     \t1) |{first_player}|
# #     \t2) | |
# #     \t3) | |{second_player}

# #     """
# # # If turn 1 in a3

# # # If turn 1 in b1
# # # If turn 1 in b2
# # # If turn 1 in b3
# # # If turn 1 in c1
# # # If turn 1 in c2
# # # If turn 1 in c3

# # print(board)

# # Verdict
# # 255,168 unique games possible. not enough time to make all combinations
# #--------------------end of brute force combinations-------------------------------#

# def check_win(board, player):
#     # Find all winning combinations
#     # List of winning combinations

#     # row wins
#     if board == "012" or board == "345" or board == "678":
#         print(f"{player} wins")

#     # column wins
#     elif board == "036" or board == "147" or board == "258":
#         print(f"{player} wins")

#     # cross wins
#     elif board == "048" or board == "246":
#         print(f"{player} wins")

# # game_play = [range(9)]
# # game_list = []
# # player = "x"
# # print(game_play)
 
# # while len(game_list) < 9: 
# #     for i in game_play:
# #         number = input("Enter a number: ")
# #         game_list += number

# #         # row wins
# #     if game_list == ['0', '1', '2'] or game_list == ['3', '4', '5'] or game_list == ['6', '7', '8']:
# #         print(f"{player} wins")

# #     # column wins
# #     elif game_list == ['0', '3', '6', ] or game_list == ['1', '4', '7'] or game_list == ['2', '5', '8']:
# #         print(f"{player} wins")

# #     # cross wins
# #     elif game_list == ['0', '4', '8'] or game_list == ['2', '4', '6']:
# #         print(f"{player} wins")

# #     print(game_list)
#---------------------------------------------------------------------------------#
