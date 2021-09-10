'''
Programming 102
Unit 2 Review
'''

"""
R ead
E valuate
P rint
L oop
"""

# ---------------------------------------------------------------------------------------- #
'''
# This REPL will only loop if the user enters exactly 'yes'
again = 'yes'

while again == 'yes':
    print("\nWelcome to the game!")

    # ...

    again = input("Do you want to play again? yes/no: ")
    
'''

# ------------------------------------------------------------------------------------------ #
'''
# This REPL displays different things for 'y', 'n' and invalid options
# but will loop unless the user enters 'n'
while True: # infinite loop

    print("\nWelcome to the game!")

    # ...
    # ...

    again = input("Do you want to play again? y/n: ")

    if again == 'y':
        print("Okay, let's play!")

    elif again == 'n':
        print('Goodbye!')
        break

    else:
        print('Invalid selection!')
'''

# ---------------------------------------------------------------------------------------- #
'''
# define lists of valid choices
valid_yes = ['y', 'yes', 'yep']
valid_no = ['n', 'no', 'nope']

# combine all the choices by concatenating two lists
valid_choices = valid_yes + valid_no


while True:
    print("\nWelcome to the game!")

    # ...

    again = input("Do you want to play again? y/n: ")

    # check to make sure the user has entered a valid choice using another REPL
    # loop until a valid choice is entered
    while again not in valid_choices:
        print("\nInvalid selection!")
        again = input("Please enter a valid choice: ")


    # once the code reaches this point,
    # the user is guaranteed to have entered a valid selection

    # check which list the user's choice is in
    if again in valid_yes:
        print("\nOkay, let's play!")

    elif again in valid_no:
        print("Goodbye!")
        break # End the loop
    
'''

# ---------------------------------------------------------------------------------- #

# Functions

# named code blocks that perform a specific task
# take in data, manipulate it, and return the result to where the function was called
# must be executed with parentheses after their name

# keyword 'def' to define a function

# variables in the parentheses ( ) are the functions 'parameters'
# parameters are empty variables, awaiting data (can also be given default values in the definition)
def add(a, b):
    return a + b # a function with a missing or blank return statement will return None by default

result = add(1, 9) + add(5, 5)
# print(result) # 20

# print(10 == add(5, 5)) # True

# 'arguments' must be passed to fill paramaters if no default values are provided
# add() # TypeError: add() missing 2 required positional arguments: 'a' and 'b'

# --------------------------------------------------------------------------------------------------- #

def punctuate(text="Hello", punctuation='.'):
    return text + punctuation

# print(punctuate('Hello', '!!!')) # Hello!!!
# print(punctuate("Hello")) # Hello. (text="Hello", punctuation=default value)
# print(punctuate()) # Hello. (both default values are used)

# print(punctuate(punctuation='???')) # Hello??? (text=default value, punctuation='???')
# print(punctuate(punctuation='?!', text='Huwuh')) # Huwuh?! (specify which parameter receives which argument)

# parameters with default values accept 'keyword arguments' (kwargs)
# kwargs specify which parameter will receive the argument

# parameters with no default values accept 'positional arguments' (args)

# ------------------------------------------------------------------------------------------------- #

def is_positive(number):
    '''
    DOCSTRING - add documentation to a function

    Describe parameters and return value

    Return False if a number is less than or equal to 0

    Return True if a number is greater than 0
    '''
    if number <= 0:
        return False
    
    return True


# print(is_positive(5)) # True

# ----------------------------------------------------------------------------------------------- #

# Scope - layers in which variables exist

# 'all the way to the left' is the 'global scope'

numbers = []
y = 500

def subtract(a, b):

    numbers.append(3.14)

    # print(y) # since subtract() and y are both defined in the global scope, y is available to subtract()

    # y += 1 # UnboundLocalError: local variable 'y' referenced before assignment

    x = 10 # x only exists in the local scope of subtract()

    return a - b

# print(x) # NameError: name 'x' is not defined

subtract(10, 2)
# print(numbers)

# ---------------------------------------------------------------------------------------------- #