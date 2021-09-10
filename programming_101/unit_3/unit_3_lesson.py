'''
Programming 101
Unit 3
'''

# datatype: boolean
# True / False

a = True
b = False

# print(a, type(a)) # True <class 'bool'>
# print(b, type(b)) # False <class 'bool'>

# in Python, booleans are Capitalized
# a = true # NameError: name 'true' is not defined

# ---------------------------------------------------------------------------------------------------- #

# Comparison Operators - compare two pieces of data and result in a boolean
# all comparisons need TWO sides


x = 5
y = 5

# = is the assignment operator

# print(x == y) # == check equality - True
# print(x != y) # != check ineqality (! means 'not') - False

# print(x < y)  # < 'strictly' less than - False
# print(x <= y) # <= less than or equal to - True

# print(x > y)  # > 'strictly' greater than - False
# print(x >= y) # >= greater than or equal to - True

# --------------------------------------------------------------------------- #

# other datatypes can be compared as well
word_1 = "cat"
word_2 = "cat"

# print(word_1 == word_2) # True

# --------------------------------------------------------------------------- #

# Logical Operators - combine two comparisons and result in a single boolean
# keywords: and, or, not

x = 5

# and - True only if BOTH comparisons are True
# print(x == 5 and x < 10) # True - both comparisons are True
# print(x == 2 and x < 10) # False - left comparison (x == 2) is False

# or - True if at least ONE comparison is True
# print(x == 2 or x < 10) # True - right comparison (x < 10) is True
# print(x == 2 or x < 0) # False - both comparisons are False

# not - flip the following boolean
# print(x > 0) # True
# print(not x > 0) # False

# 'not' is often used with the keyword 'in' to determine if an item is 'in' a sequence
# 'in' results in a boolean
# print('k' in 'book') # True
# print('z' not in 'book') # True

# -------------------------------------------------------------------------------------- #

# Conditional Statments - run different 'code blocks' based on the outcome of comparisons
# keywords: if, elif, else

# code block - a section of code that executes together. 
#              In Python, code blocks are defined using horizontal indentation

"""
Conditional Statements
----------------------

- must start with if
- every single if will be checked
- elif will only be checked if the preceding if  and other elifs were False
- else will run if all other conditions were False

- if/elif will only be checked until a True condition is found
"""

'''
if/elif combos
--------------

if
if / elif
if / else
if / elif / else
if / elif / elif / ... / elif
if / elif / elif / ... / else
'''

# ----------------------------------------------------------------------------- #
'''
x = 10
y = 10

if x < y: # colon signifies the start of a code block
    # first line of the code block sets the indentation for the block
    # all other lines in the code block must match the first line's indentation
    print(f'{x} is less than {y}')

elif x == 14: # elif requires a condition as well
    print('x equals 14')

elif x > y:
    print(f'{x} is greater than {y}')

else: # doesn't require a condition because it catches all other cases
    print(f'x and y are both {x}')
'''
# --------------------------------------------------------------------------------- #
# PRETEND THAT THIS IS THE TOP OF THE FILE...

import random

# Guess the number
'''
# set the secret number
# secret = 5 # (for testing)
secret = random.randint(1, 10)

# ask the user to guess a number
guess = input("Please guess a number between 1 and 10: ")

# convert the guess to an integer
guess = int(guess)

# check the guess
if guess == secret:
    message = f'Congratulations! You guessed the secret number: {secret}!'

elif guess < secret:
    message = f'Oops! Your guess of {guess} was too low! The secret was {secret}...'

elif guess > secret:
    message = f'Oops! Your guess of {guess} was too high! The secret was {secret}...'

print(message)

'''