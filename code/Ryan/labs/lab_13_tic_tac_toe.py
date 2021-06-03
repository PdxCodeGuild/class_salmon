# --------------------------------------------------------------------------------------#

def main(user_inputs):
    # Read
    
    pass


class Game:
    def __init__(self): # this is the initializer
        self.board = ["1","2","3","4","5","6","7","8","9"] # these are member variables
        
    # Function to print Tic Tac Toe
    def __repr__(self):
        values = self.board
        line   = "\t{}|{}|{}".format(values[0], values[1], values[2])
        line_2 = "\t{}|{}|{}".format(values[3], values[4], values[5])
        line_3 = "\t{}|{}|{}".format(values[6], values[7], values[8])
        return line + "\n" + line_2 + "\n" + line_3


game = Game()
print(game)

class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token

player1 = Player("player1","x")
player2 = Player("player2","o")

#print(player1.name)
#print(player1.token)

# --------------------------------------------------------------------------------------#

# Show board with coordinates
# Which player turn is it?
# Pick coordinate of the board
# Check if something exists on the board
# If not, add letter
# If Else, try again
# Increase counter. 
# If counter hits 9, max tries exceeded
# Add the letter to the board
# Change to other player

firstfirst_player = ""

pick_player = input("Whose turn? (x or o): ")

if pick_player != "x":
    first_player = "o"
else:
    first_player = pick_player

print(f"Current Player: {first_player}")

board = f"""

\t  a|b|c

\t1) | | 
\t2) | |
\t3) | |

"""

print(board)

first_move = input("Pick a coordinate: ")

if first_move == "a1":
    board = f"""

    \t  a|b|c

    \t1){first_player}| | 
    \t2) | |
    \t3) | |

    """
elif first_move == "a2":
    board = f"""

    \t  a|b|c

    \t1) |{first_player}| 
    \t2) | |
    \t3) | |

    """
elif first_move == "a3":
    board = f"""

    \t  a|b|c

    \t1) ||{first_player}
    \t2) | |
    \t3) | |

    """
elif first_move == "b1":
    board = f"""

    \t  a|b|c

    \t1) || 
    \t2){first_player}| |
    \t3) | |

    """
elif first_move == "b2":
    board = f"""

    \t  a|b|c

    \t1) || 
    \t2) |{first_player}|
    \t3) | |

    """
elif first_move == "b3":
    board = f"""

    \t  a|b|c

    \t1) || 
    \t2) | |{first_player}
    \t3) | |

    """
elif first_move == "c1":
    board = f"""

    \t  a|b|c

    \t1) || 
    \t2) | |
    \t3){first_player}| |

    """
elif first_move == "c2":
    board = f"""

    \t  a|b|c

    \t1) || 
    \t2) | |
    \t3) |{first_player}|

    """
elif first_move == "c3":
    board = f"""

    \t  a|b|c

    \t1) || 
    \t2) | |
    \t3) | |{first_player}

    """
else:
    "Position doesn't exist"
print(board)

current_board = board

second_player = ""

pick_player = input("Whose turn? (x or o): ")

if pick_player != "x":
    second_player = "o"
else:
    second_player = pick_player

print(f"Current Player: {second_player}")

print(current_board)

second_move = input("Pick a coordinate: ")

if second_move == "a2" and first_move == "a1":
    board = f"""

    \t  a|b|c

    \t1){first_player}|{second_player}| 
    \t2) | |
    \t3) | |

    """
elif second_move == "a3" and first_move == "a1":
    board = f"""

    \t  a|b|c

    \t1)|{first_player}|{second_player}
    \t2) | |
    \t3) | |

    """   
elif second_move == "b1" and first_move == "a1":
    board = f"""

    \t  a|b|c

    \t1){first_player}||
    \t2){second_player}| |
    \t3) | |

    """   
elif second_move == "b2" and first_move == "a1":
    board = f"""

    \t  a|b|c

    \t1){first_player}||
    \t2)|{second_player}|
    \t3) | |

    """   
elif second_move == "b3" and first_move == "a1":
    board = f"""

    \t  a|b|c

    \t1){first_player}||
    \t2)| |{second_player}
    \t3) | |

    """   
print(board)