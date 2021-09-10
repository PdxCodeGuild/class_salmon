'''
Programming 102
Unit 1 Review
'''

import random

'''
Anatomy of an Error Message
---------------------------


Traceback (most recent call last):
  File "<FILENAME>.py", line number (approx)
    troublesome code (approx)
                   ^

ErrorType: specific error message
'''

# SyntaxError - a piece of code is missing
# 'abc # SyntaxError: EOL while scanning string literal (missing closing quotation mark)
# print('hello'] # SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
# 10 / # SyntaxError: invalid syntax

# -------------------------------------------------------------------------------------------- #

# NameError - variable or function name was used that isn't defined

# balloon # NameError: name 'balloon' is not defined
# Print() # NameError: name 'Print' is not defined

# -------------------------------------------------------------------------------------------- #

# IndentationError - inconsistent horizontal placement
'''
 x = 4 # IndentationError: unexpected indent

if x < 10:
    print("hello")
     print("hello") # IndentationError: unexpected indent
  print("hello") # IndentationError: unindent does not match any outer indentation level


for x in range(10):
    # empty code block
    # pass - keyword to allow a blank code block


print(x) # IndentationError: expected an indented block
'''

# ------------------------------------------------------------------------------------------- #

# TypeError - wrong datatype was used in an operation
# '5' + 5 # TypeError: can only concatenate str (not "int") to str
# [10, 20, 30] / 10 # TypeError: unsupported operand type(s) for /: 'list' and 'int'
# 123[0] # TypeError: 'int' object is not subscriptable
# len(456) # TypeError: object of type 'int' has no len()

# ------------------------------------------------------------------------------------------- #

# AttributeError - variable, function or method doesn't belong to an object
# random.imaginary_function() # AttributeError: module 'random' has no attribute 'imaginary_function'
# 'abc'.append('d') # AttributeError: 'str' object has no attribute 'append'
# ['a', 'b', 'c'].capitalize() # AttributeError: 'list' object has no attribute 'capitalize'

# ------------------------------------------------------------------------------------------- #

# ValueError - proper datatype, but improper value was used
# int('fish') # ValueError: invalid literal for int() with base 10: 'fish'
# float('fish') # ValueError: could not convert string to float: 'fish'

# -------------------------------------------------------------------------------------------- #

# ZeroDivisionError - divide by 0
# 1 / 0 # ZeroDivisionError: division by zero

# ------------------------------------------------------------------------------------------- #

# sometimes error are triggered in different files and will need to be tracked down
# random.choice(99)
'''
Traceback (most recent call last):
  File "C:/Users/keego/Desktop/pdx_code_day/programming_102/unit_2/unit_1_review.py", line 82, in <module>         <module>
    random.choice(99)
  File "C:/Users/keego/AppData/Local/Programs/Python/Python39/lib/random.py", line 346, in choice
    return seq[self._randbelow(len(seq))]
TypeError: object of type 'int' has no len()
'''

# --------------------------------------------------------------------------------------------- #

# Handling Errors
# keywords: try, except, else, finally

"""
try:
    # try to run the code in this block
    # if an error is raised in this block
    # it can be caught and handled using an 'except' block

except ErrorType:
    # 'ErrorType' is the specific type of error we wish to catch
    # run this code block if the specified ErrorType was raised in the 'try' block

else:
    # run this code block if no error was raised in the 'try' block

finally:
    # run this code block no matter what (error or no error)
"""

# ------------------------------------------------------------------------------ #

'''
while True: # infinite loop, requiring 'break' to end
    try:
        x = input("\nEnter a number for x: ")
        y = input("Enter a number for y: ")

        x = float(x)
        y = float(y)

        quotient = x / y

    except ValueError:
        # if x or y cannot be converted to float
        print(f'\nOne of the numbers cannot be converted to float: {x}, {y}')

    # multiple except blocks for multiple errors
    except ZeroDivisionError:
        print('\nCannot divide by zero!!!')

    else:
        # if no error was raised
        print(f'\n{x} / {y} = {quotient}')
        break # end the while loop

    finally:
        print("\nYay, Python!")
'''

