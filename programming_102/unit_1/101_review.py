'''
Programming 102
101 Review
'''

# define a variable 'animal' and assign the string 'dog' to it using =
# = is the assignment operator - assign the value on the right to the variable on the left
animal = 'dog'
# print(animal) # dog

# --------------------------------------------------------------------------------------- #

# a "function" is a named code block that performs a certain task
# functions are executed by placing parentheses () after their name
# data can be passed into the function by placing it within the parentheses
# functions will always return a value as well

# print(data) - display the data in the terminal

# print('hello world') # hello world

# type(object) - return the datatype of the object (everything in Python is an object)
# print(type(animal)) # <class 'str'>

# string (str) - a sequence of textual characters surrounded by quotes

# ------------------------------------------------------------------------------------------ #

# concatenation - adding strings together to form a single string

# change the value within the animal variable to 'cat'
animal = 'cat'

# add the string 'fish' to the value within the variable 'animal'
animal = animal + 'fish'
# print(animal) # catfish

animal += 'es' # same as 35
# print(animal) # catfishes

# ---------------------------------------------------------------------------------------- #

# a 'method' is a function that manipulates only the object to which it belongs
# everything in Python is an object
# an object's methods are accessed using dot notation (. after the name)

# .upper() - return an uppercase version of the string
# print(animal.upper()) # CATFISHES

banner = ' PDX CODE GUILD '.center(50, '*')
# print(banner) # ***************** PDX CODE GUILD *****************

# methods can be chained. Each one operates on the return value of the previous
# print(banner.replace('*', '#').lower()) # ################# pdx code guild #################

# --------------------------------------------------------------------------------------- #

# escape characters
# denoted with a backslash \ before the character
# and "escape" the normal rules of strings

# "hello "world"" # Error! Quotes cancel each other

# Solution 1:
# print('hello "world"') # hello "world" - printing quotes with mismatched sets

# Solution 2:
# print("hello \"world\"") # hello "world" - printing quotes using escape characters

# ------------------------------------ #

# formatting strings
# print("A\nB\nC") # \n - new line character

# print("A\tB\tC") # \t - horizontal tab character

# ---------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------- #

'''
Unit 2
'''

'''
Python Variable Names

- must start with a letter or underscore
- cannot start with a number
- can only contain alphanumeric characters and underscores (A-z, 0-9, and _)
- are case sensitive (age, Age, AGE are 3 different variables)
'''

# python_variable_and_function_names_use_snake_case
# lowercase words separated with underscores

# ThisIsTitleOrPascalCase - used in Python for defining classes
# ALLCAPS - generally represent constant variables

# For Python styling conventions, check out PEP8 (Python Style Guide)

# ---------------------------------------------------------------------------------- #

# f-string
# 'f' stands for 'formatted'. f-strings allow Python expressions to be placed within a string

# f-strings begin with an 'f' before the opening quote
# Expressions are placed within the string using curly brackets {}

number = 99.0
numbers = [11, 22, 33]

# Error! Concatenation only works between strings
# other datatypes will need to be typecast using str() before concatenation
message = "The number is " + str(number) + '. The numbers are ' + str(numbers) + '.'
# print(message)

# f-strings don't care about datatype
message = f'The number is {number}. The numbers are {numbers}.'
# print(message)

# -------------------------------------------------------------------------------------------- #

'''
user_string = input(prompt_message)

Print the prompt_message and wait for the user to hit enter.
Once the user hits enter, anything they typed in the terminal will be returned.
Return value can be saved in a variable such as 'user_string' above.

name = input("Enter your name: ")
print(f"Welcome, {name}!")
'''

# ---------------------------------------------------------------------------------------------------- #
'''
# input() always returns a string

number = input('Enter a number: ')

print(number, type(number)) # 7 <class 'str'>
print(number * 10) # 7777777777

# typecast to a number
# int(object) - return the object as an integer (whole number), if possible
# float(object) - return the object as a float (decimal number), if possible

# convert the string to float
number = float(number)

print(number, type(number)) # 7.0 <class 'float'>
print(number * 10) # 70.0
'''
# ------------------------------------------------------------------------------------------------- #

x = 5
y = 3

# arithmetic operators

# print(x + y)  # addition +
# print(x - y)  # subtraction -

# print(x * y)  # multiplication
# print(x ** y) # exponentiation **

# print(x / y)  # 'regular' division / (results in a float)
# print(x // y) # 'floor' division // (always round down to the nearest integer)

# print(x % y)  # modulus % (remainder after division)

# ----------------------------------------------------------------------------------------- #

x = 2

x + 5 # uses x but doesn't change it
# print(x + 5) # 7 - uses x but doesn't change it
# print(x) # 2

# add 5 to x and save the result over the previous value
x = x + 5

# print(x) # 7

# ReAssignment Operators
x += 5 # x = x + 5
# print(x) # 12

# There are reassignment operators for all arithmetic operators
x /= 10
# print(x) # 1.2

# ----------------------------------------------------------------------------------------------- #

'''
Unit 3
'''

# boolean
# True/False

a = True
b = False
 
# print(a, type(a)) # True <class 'bool'>
# print(b, type(b)) # False <class 'bool'>

# booleans are Capitalized in Python
# a = false # NameError: name 'false' is not defined

# ------------------------------------------------------------------------------------------- #

# Comparison Operators - compare two pieces of data and result in a boolean
# ALL comparisons need two sides

x = 5
y = 5

# print(x == y)  # == check equality - True
# print(x != y)  # != check inequality - False

# print(x < y)  # 'strictly' less than - False
# print(x <= y) # less than or equal to - True

# print(x > y)  # 'strictly' greater than - False
# print(x >= y) # greater than or equal to - True

# ------------------------------------------------------------------------ #

# Logical Operators - combine comparisons and result in a single boolean
# keywords: and, or, not

# logical statements need TWO comparisons

x = 5

# and - True only if BOTH comparisons are True
# print(x == 5 and x < 10) # True - both comparisons are True
# print(x == 2 and x < 10) # False - left comparison (x == 2) is False

# or - True if at least ONE comparison is True
# print(x == 2 or x < 10) # True - right comparison (x < 10) is True
# print(x == 2 or x < 0) # False - both comparisons are False

# not - flip a boolean
# print(x < 0) # False
# print(not x < 0) # True

# ------------------------------------------------------------------------------------------------- #
"""
# conditional statements - run different code blocks based on the outcome of comparisons
# if, elif, else

# code block - a section of code that executes together.
#              In Python, code blocks are defined using horizontal indentation

x = 14
y = 14

if x < y: # colon signifies the start of a code block
    # first line of the code block sets the indentation for the block
    print(f"{x} is less than {y}")

elif x == 15:
    print('x equals 15')

elif x > y: # elif also requires a condition
    print(f"{x} is greater than {y}")

else: # doesn't require a condition
    print(f'x and y are both {x}')

"""

# ----------------------------------------------------------------------------------------- #

'''
Unit 4
'''


'''
Lists are 'ordered' and 'changeable' sequences of items.
Lists are create using square brackets []
List items are separated with commas ,
'''

colors = ['red', 'green', 'blue']

# organized vertically
colors = [
    'red',
    'green',
    'blue'
]

# print(colors) # ['red', 'green', 'blue']

# ------------------------------------------------------------------------------------------- #

# because they are ordered, list items can be retrieved
# using their position ('index') in the list.

# place the index in square brackets to retrieve the item
# list indices always start at 0

# print(colors[0]) # red
# print(colors[1]) # green
# print(colors[2]) # blue

# cannot use non-existent indices
# print(colors[3]) # IndexError: list index out of range

# In Python, negative indices are allowed
# -1 will always be the last index

# print(colors[-1]) # blue
# print(colors[-2]) # green
# print(colors[-3]) # red

# can't use non-existent indices
# print(colors[-4]) # IndexError: list index out of range

# ---------------------------------------------------------------------------- #

# strings are also 'ordered' sequences
letters = 'ABCD'
# print(letters[0]) # A

# however, strings are immutable (not 'changeable')
# letters[0] = 'Z' # TypeError: 'str' object does not support item assignment

# lists ARE mutable (changeable)
colors[1] = 'yellow'
# print(colors) # ['red', 'yellow', 'blue']

# ------------------------------------------------------------------------- #

# cannot add values this way
# colors[3] = 'purple' # IndexError: list assignment index out of range

# add items using list methods

# .append(item) - add a single item to the end of the list
colors.append('purple')
# print(colors) # ['red', 'yellow', 'blue', 'purple']

# .insert(index, item) - add the item at the index
colors.insert(1, 'pink')
# print(colors) # ['red', 'pink', 'yellow', 'blue', 'purple']

# .extend(sequence) - add the items from the sequence to the end of the list
colors.extend(['yellow', 'orange'])
# print(colors) # ['red', 'pink', 'yellow', 'blue', 'purple', 'yellow', 'orange']

# ----------------------------------------------------------------------------------------- #

# removing items from a list

# .remove(item) - remove the first occurrence of the item from the list
colors.remove('yellow')
# print(colors) # ['red', 'pink', 'blue', 'purple', 'yellow', 'orange']

# .pop(index) - remove the item at the index and return it. index defaults to -1 if not provided
# colors.pop() # remove the last item
# print(colors) # ['red', 'pink', 'blue', 'purple', 'yellow']

# colors.pop(1) # remove the item at index 1
# print(colors) # ['red', 'blue', 'purple', 'yellow']

# ----------------------------------------------------------------------------------------------- #

# .sort() - sort a list in ascending order, in place. (returns None)
# doesn't return a sorted list

# colors = colors.sort() # DON'T DO THIS
# print(colors) # None - .sort() returns None
# print(colors[0]) # TypeError: 'NoneType' object is not subscriptable

# DO THIS
colors.sort()
# print(colors) # ['blue', 'orange', 'pink', 'purple', 'red', 'yellow']

# ---------------------------------------------------------------------------------------- #

# loop - code block that repeats until a certain condition is met

# for item in sequence - loop through each item in a sequence

# for / in - Python keywords
# item - arbitrary variable name to store each item as the loop visits it
# sequence - string, list, or other iterable (loopable) object

'''
for color in colors:
    # repeat this code block for each color in the list
    print(color)
'''

# ---------------------------------------------------------------------------------- #

# for x in range() - loop a certain number of times

# range(stop) - return a range of numbers from 0 to stop-1
 
# print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

'''
for x in range(11):
    print(2 ** x)

'''

# ------------------------------------------------------------------------------------------- #

# while loop
'''
while some_condition == True:
    # loop this
    # code block
    # ...
'''

'''
x = 0
while x < 10:
    print(x)
    x += 1

'''

# ---------------------------------------------------------------------------------------------- #

# loop controls
# else, continue, break

for x in range(10):

    # skip the evens
    if x % 2 == 0:
        # print("...even...")
        continue

    if x == 8:
        print("Goodbye!")
        break # end the loop immediately

    print(x)

else:
    print("The loop made it all the way through!")
