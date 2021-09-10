'''
Programming 101
Unit 3 Review
'''

# Datatype: Boolean
# True/False

a = True
b = False

# print(a, type(a)) # True <class 'bool'>
# print(b, type(b)) # False <class 'bool'>

# tries to use 'false' as a variable name 
# a = false # NameError: name 'false' is not defined

# ------------------------------------------------------------------------------- #

# all datatypes have typecasting functions
# str(), int(), float()

# bool(object) - return a boolean representation of the object

# Truthy/Falsey
# If an object has value, it will convert to True
# If an object has NO value, it will convert to False

x = 0 # False - zero has no value
y = 1 # True - one (or any number other than zero) has value

x = '' # False - blank string has no value
y = 'z' # True - string with at least one character has value

x = [] # False - empty list has no value
y = [11, 22, 33] # True - list with at least one item has value

# print(bool(x))
# print(bool(y))

# ---------------------------------------------------------------------------------- #

# Comparison Operators - compare two pieces of data and result in a boolean

x = 5
y = 5

# print(x == y) # == equality - True
# print(x != y) # != inequality - False

# print(x < y)  # < 'strictly' less than - False
# print(x <= y) # <= less than or equal to - True

# print(x > y)  # > 'strictly' greater than - False
# print(x >= y) # >= greater than or equal to - True

# -------------------------------------------------------------------------------- #

# other datatypes can be compared
# print('cat' == 'dog') # False
# print('abc' == 'abc') # 'abc'

# avoid < & > with datatypes other than strings (at least for now)
# they can cause strange results
# print('a' < 'A') # False?

# check if letters are in alphabetical order (if they're both upper or lowercase)
# print('a' < 'h') # True
# print('t' < 'b') # False

# ------------------------------------------------------------------------------ #

# Logical Operators - combine two comparisons and result in a single boolean
# and, or, not

x = 2

# and - True only if BOTH comparisons are True
# print(x == 2 and x < 10) # True - both comparisons are True
# print(x == 3 and x < 10) # False - left comparison (x == 3) is False

# or - True if at least ONE comparison is True
# print(x == 30 or x < 10) # True - right comparison (x < 10) is True
# print(x == 30 or x < 0) # False - both comparisons are False

# all logical statments need TWO comparisons
x = 2
y = 5
# print(x > 10 and  < 20) # Error! Right comparison is missing its left side. Should be x < 20
# print(x > 10 or y) # 5


# not - flips the boolean
# print(x > 0) # True
# print(not x > 0) # False

# 'not' works in front of any code that produces a boolean
# .isnumeric() - string method which returns a boolean indicating if the string is all numbers or not
string='1a23'

# print(string.isnumeric()) # False
# print(not string.isnumeric()) # True

# ------------------------------------------------------------------------------------------ #

# 'not' with Truthy/Falsey
word = ''

# These both check if the word variable contains a blank string
# print(word == '') # True
# print(not word) # True

# ------------------------------------------------------------------------------------------- #

# Conditional Statements - run different code blocks based on the outcome of comparisons
# if, elif, else

# code block - a section of code that executes together.
#              In Python, code blocks are defined using indentation

'''
Conditional Statements

- must start with if
- every single if will be checked
- elif will only be checked if the preceding if and other elifs were False
- else will run if all other conditions were False

- conditionals will only be checked until a True condition is found
'''

'''
if
if / elif
if / else
if / elif / else
if / elif / elif / ... / elif
if / elif / elif / ... / else
'''

# ------------------------------------------------------------------------------------ #

light_switch = 'ON'

if light_switch == 'ON':
    message = "I can see!"

elif light_switch == 'OFF':
    message = "It's dark in here!"

# print(message)

# -------------------------------------------------------------------------------------- #
"""
# ask the user for a color
color = input("Enter a color: ")

# check the user's color
if color == 'green' or color == 'red':
    print(f"I like the color {color}")

elif color == 'yellow' or color == 'teal':
    print(f"{color.upper()}!!!")

# check if a particular character is in the string
elif 'p' in color: 
    print(f"{color.capitalize()} contains the letter 'p'")

# elif color == '':
elif not color: # same as line 169
    print("Color cannot be blank")

else:
    print(f"I'm indifferent to the color {color}...")

"""

# ------------------------------------------------------------------------------------ #

# 'nested' if/elif structures

x = 10

if x < 10:
    output = f'{x} is less than 10'

    # nested if/elif
    if x == 5:
        output += '. x is 5'
        
    elif x > 5:
        output += f'. {x} is greater than 5'

    elif x < 5:
        output += f'. {x} is less than 5'

else:
    if x > 10:
        output = f'{x} is greater than 10'

    elif x == 10:
        output = 'x is 10.'

print(output)