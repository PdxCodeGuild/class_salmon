'''
Programming 102
Unit 2
'''

import random
from string import ascii_uppercase as uppercase

'''
R ead
E valuate
P rint
L oop
'''

# ---------------------------------------------------------------------------------------- #

'''
# This REPL will only loop if the user enters exactly 'yes'

play_again = 'yes' # loop control
while play_again == 'yes':
    # loop this code block
    print("\nWelcome to the game!")


    # ...
    # ... other code ...
    # ...


    # allow the user to redefined the play_again variable to determine if the loop should continue
    play_again = input("Do you want to play again? yes / no: ")

else:
    print("\nThanks for playing!")
'''

# ----------------------------------------------------------------------------------------- #
'''
# This REPL quits if the user enters 'done', but loops otherwise
while True: # infinite loop, requires 'break' to end

    # ask the user for a color or if they want to quit:
    color = input("Please enter a color or 'done' to quit: ")

    # check if the user entered 'done' and wants to quit
    if color == 'done':
        print("Thanks for playing!")
        break # end the loop

    # do something here with the user's input
    print(f"Thanks for entering the color '{color}'!")

'''

# ------------------------------------------------------------------------------------------ #

# Functions!

# built-in functions
# print(), type(), input(), int(), str(), float(), list(), bool(), len()

'''
Functions

- are named code blocks
- run only when called upon
- typically designed to perform a single task
- once they're defined, they can be called as many times as needed with different data
- receive data to use & return data after they've manipulated it
- are variables that store code blocks instead of single values
'''

# --------------------------------------------------------------------------------------- #

# functions are defined using the keyword 'def'
'''
def function_name(parameter1, parameter2, etc...):
    # this code block will run
    # when the function is 'called'

    # manipulate parameters somehow...

    # send the data back to the line where the function was called
    # with the keyword 'return'
    return manipulated_parameters


# 'call' the function and save the return value in a variable
data_returned_from_function = function_name(argument1, argument2, etc...)
# data passed to a function to fill its parameters are called 'arguments'

'''

# --------------------------------------------------------------------------------------- #

# increment(number) - add one to the number and return the result

def increment(number):
    return number + 1

# call the increment function with a value for 'number' and save the return value in a variable
result = increment(99)
# print(result) # 100

result = increment(result)
# print(result)

# --------------------------------------------------------------------------------- #

count = 0

while count < 10:
    # print(count)

    # use the increment function to increment the count
    count = increment(count)

# --------------------------------------------------------------------------------- #

# arguments MUST be passed to fill parameters (unless default values are provided)
# increment() # TypeError: increment() missing 1 required positional argument: 'number'

# ----------------------------------------------------------------------------------- #

# return the sum of two numbers
def add(a=10, b=1):
    return a + b

# if NO default values are provided:
# add() # TypeError: add() missing 2 required positional arguments: 'a' and 'b'
# add(2) # TypeError: add() missing 1 required positional argument: 'b'
# print(add(2, 4)) # a = 2, b = 4

# If default values are provided for parameters:
# print(add(9)) # a = 9, b = default
# print(add()) # a = 10, b = 1 (both defaults used)
# print(add(100, 15)) # a = 100, b = 15 (override defaults)
# print(add(b=13)) # a = default, b = 13
# print(add(b=2, a=5)) # b = 2, a = 5

# ------------------------------------------------------------------------------------ #

# 'shred' a string and return a randomized list of its characters

def paper_shredder(string):
    
    # convert the string to a list
    characters = list(string)

    # randomize the list
    random.shuffle(characters)

    # return the randomized list
    return characters


# shredded = paper_shredder('AAAABBCCCC')
# shredded = paper_shredder('####^^^^^*****$$$$@@@@')
# shredded = paper_shredder(uppercase)

# print(shredded)

# ----------------------------------------------------------------------------------- #

# generate a list of 'limit' integers between 'low' and 'high'

def generate_random_numbers(limit, low=0, high=100):
    # create a blank list to store numbers
    numbers = []
    
    # loop 'm' times
    for number in range(limit):
        # generate a random integer between low and high
        random_number = random.randint(low, high)
        
        # add the number to the list
        numbers.append(random_number)

    # return the list
    return numbers




numbers = generate_random_numbers(10) # 10 numbers between 0 and 100
numbers = generate_random_numbers(5, 10, 20) # 5 numbers between 10 and 20
numbers = generate_random_numbers(1000, -100, 100) # 1000 numbers between -100 and 100

# print(numbers)

# -------------------------------------------------------------------------------------- #

# return True if the number is positive
# return False if the number is negative or 0

def is_positive(number):
    # if the number is positive, return True
    if number > 0:
        return True

    # if the number is not positive, return False
    return False

# print(is_positive(-9))
# print(is_positive(9))

# --------------------------------------------------------------------------------------- #

numbers = generate_random_numbers(100, -100, 100)
# print(numbers)

# count the number of positive numbers
positives = 0

# loop through each number
for number in numbers:
    # if the return value from is_positive is True
    if is_positive(number): #  == True:
        # add one to the count
        positives = increment(positives)

# print(numbers)
# print(f"There are {positives} positive numbers in the list.")

# ---------------------------------------------------------------------------------------- #