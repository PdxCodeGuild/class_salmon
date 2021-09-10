'''
Programming 101
Unit 4
'''

import random

'''
List

'Ordered' and 'changeable' sequences of items.
Items are separated with commas
Lists are defined using square brackets []

Since lists are 'ordered', their items can be retrieved using their positions in the list
An item's position in the list is called its 'index' (indices plural)
'''

# define an empty list
empty_list = []
# print(empty_list, type(empty_list)) # [] <class 'list'>

# -------------------------------------------------------------------------------------- #

numbers = [22, -11, 33, -44] # list of integers
colors = ['red', 'green', 'blue'] # list of strings

# list items can be ANY datatype, including other lists
jumble = ['cat', 99, True, 3.14, None, [1, 2, 3]]
# print(jumble) # ['cat', 99, True, 3.14, None, [1, 2, 3]]

# ---------------------------------------------------------------------------------------- #

# list items can be organized vertically as well
colors = [
    'red',
    'green',
    'blue',
]
# print(colors) # ['red', 'green', 'blue']

# ---------------------------------------------------------------------------------------- #

# retreive an item from the list using its index
# place the index in square brackets after the list's variable name
# list indices always start at 0

# print(colors[0]) # red
# print(colors[1]) # green
# print(colors[2]) # blue

# can't use indices that don't exist
# print(colors[3]) # IndexError: list index out of range

# the last index in a list is one less than the list's length

# ------------------------------------------------------------------------------------- #

# python allows negative indices
# -1 will always be the last index
# print(colors[-1]) # blue
# print(colors[-2]) # green
# print(colors[-3]) # red

# can't use indices that don't exist
# print(colors[-4]) # IndexError: list index out of range

# ----------------------------------------------------------------------------------------- #

# strings are 'ordered' sequences as well
letters = 'ABC'
# print(letters[0]) # A

# strings are NOT 'changeable'
# letters[0] = 'Z' # TypeError: 'str' object does not support item assignment

# in order to change a string, we must produce a NEW string with the changes made
letters = letters.replace('A', 'Z')
# print(letters)

# typecast the string to a list
letters = list(letters)
# print(letters) # ['A', 'B', 'C']

# lists ARE 'changeable'
letters[0] = 'Z'
# print(letters) # ['Z', 'B', 'C']

# -------------------------------------------------------------------------------------- #

# change the color at index 1 to 'yellow'
colors[1] = 'yellow'
# print(colors) # ['red', 'yellow', 'blue']

# cannot add items this way
# colors[3] = 'purple' # IndexError: list assignment index out of range

# ------------------------------------------------------------------------------------ #

# add items using list methods

# .append(item) - add a single item to the END of the list
colors.append('purple')
# print(colors) # ['red', 'yellow', 'blue', 'purple']

# .insert(index, item) - add the item at the index
colors.insert(1, 'teal')
# print(colors) # ['red', 'teal', 'yellow', 'blue', 'purple']

# .extend(sequence) - add the items from the sequence to the original list
colors.extend(['yellow', 'mauve'])
# print(colors) # ['red', 'teal', 'yellow', 'blue', 'purple', 'yellow', 'mauve']

# ---------------------------------------------------------------------------------------- #

# delete items from a list

# .remove(item) - remove the first occurrence of the item from the list
# print(colors) # ['red', 'teal', 'yellow', 'blue', 'purple', 'yellow', 'mauve']
colors.remove('yellow')
# print(colors) # ['red', 'teal', 'blue', 'purple', 'yellow', 'mauve']

# .pop(index) - remove the item at the index and return it. index defaults to -1 if not provided
# colors.pop() # remove the last item
# print(colors) # ['red', 'teal', 'blue', 'purple', 'yellow']

# colors.pop(0) # remove the first item
# print(colors) # ['teal', 'blue', 'purple', 'yellow']

# --------------------------------------------------------------------------------------- #

# random.choice(sequence) - return a random selection from the sequence

# select a random color from the colors list
random_color = random.choice(colors)
# print(random_color)

ABCs = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
random_letter = random.choice(ABCs)
# print(random_letter)

# ------------------------------------------------------------------------------------- #

# loop - code block that repeats until a certain condition is met

# 'for' loop

# for item in sequence - loop through each item in a sequence

'''
for/in - Python operators
item - variable with an arbitrary name which will hold each item from the sequence as it's visisted
sequence - iterable object (list, string, etc...) through which to loop
iterable = loopable
'''

colors = ['red', 'teal', 'blue', 'purple', 'yellow', 'mauve']

'''
for color in colors:
    # loop this code block
    # until all the colors in the list have been visited
    print(color)
'''

# --------------------------------------------------------------------------------------------- #

counter = 1 # to label the colors

for color in colors:
    output = f'{counter}. {color}'

    # print(output)

    # increment the counter to increase the color label number
    counter += 1

# ------------------------------------------------------------------------------------------- #

# use a string as a sequence for looping

vowels = ['A', 'E', 'I', 'O', 'U']

# loop through each letter in the string
for letter in ABCs:
    # check if the letter is a vowel
    if letter in vowels:
        output = f'*** {letter} is a vowel'

    else:
        output = letter

    # print(output)

# -------------------------------------------------------------------- #

# for x in range() - loop a certain number of times

# range(stop_value) - return a range of numbers from 0 to stop_value-1

# print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# loop 10 times
'''
for x in range(10):
    print(x)
'''

# ----------------------------------------------------------------------------------- # 

# generate a list of 10 random integers between 0 and 100

# blank list of numbers
numbers = []

for x in range(10):
    # generate a random integer between 0 and 100
    random_number = random.randint(0, 100)

    # add the number to the list
    numbers.append(random_number)

    # print(numbers) # print the list after each item is added

# print(numbers) # [10, 55, 89, 90, 71, 82, 17, 18, 80, 41]

# ------------------------------------------------------------------------ #

# square each number in the list 

numbers_squared = []

for number in numbers:
    # square the current number
    number_squared = number ** 2

    # add the squared number to the list
    numbers_squared.append(number_squared)

# print(numbers) # [10, 29, 46, 90, 68, 63, 17, 34, 45, 3]
# print(numbers_squared) # [100, 841, 2116, 8100, 4624, 3969, 289, 1156, 2025, 9]

# ------------------------------------------------------------------------------- #

powers_of_2 = []

# generate a list of powers of 2 from 0 to 10

for exp in range(11):
    # raise 2 to the power of exp and add it to the list
    powers_of_2.append(2 ** exp)

# print(powers_of_2)