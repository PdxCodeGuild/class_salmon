'''
Programming 101
Unit 4 Review
'''
import random


'''
Lists are 'ordered' and 'changeable' sequences of items.
Items are separated with commas. Lists are defined using square brackets []
'''

fruits = ['apple', 'banana', 'orange']
# print(fruits) # ['apple', 'banana', 'orange']

# list items can be ANY datatype, including other lists
jumble = [True, None, 73, 1.1, [1, 2, 3], 'cat']

# list items can be organized vertically
fruits = [
    'apple',
    'banana',
    'orange',
]
# print(fruits) # ['apple', 'banana', 'orange']

# ---------------------------------------------------------------------------------- # 

# because lists are 'ordered', their items
# can be retrieved using their positions in the list
# an item's position in the list is called its 'index'
# list indices always start at 0

# place an item's index in square brackets after the list name to get the value at that index
# print(fruits[0]) # apple
# print(fruits[1]) # banana
# print(fruits[2]) # orange

# cannot use indices that don't exist
# print(fruits[3]) # IndexError: list index out of range

# --------------------------------------- #

# In Python, negative indices are allowed
# -1 will be the index of last item in the list
# print(fruits[-1]) # orange
# print(fruits[-2]) # banana 
# print(fruits[-3]) # apple

# cannot use indices that don't exist
# print(fruits[-4]) # IndexError: list index out of range

# ----------------------------------------------------------------------------------------- #

# last index of a list is one less than the list's length
# len(sequence) - return the length of the sequence as an integer

# print(len(fruits)) # 3

# calculate the last index using the length
last_index = len(fruits) - 1
# print(last_index, fruits[last_index]) # 2 orange

# ------------------------------------------------------------------------------------------- #

# strings are also 'ordered' sequences
# indices can be used to retrieve each character
letters = 'ABCDEFG'
# print(letters[1]) # B

# however, strings are not 'changeable' (immutable)
# letters[0] = 'Z' # TypeError: 'str' object does not support item assignment

# ------------------------------------------------------------------------------------------ #

# lists ARE changeable (mutable). Their items can be given new values / rearranged
fruits[0] = "lime"
# print(fruits) # ['lime', 'banana', 'orange']

# -------------------------------------------------------------------------------------------- #

# cannot add items this way
# fruits[3] = 'lemon' # IndexError: list assignment index out of range

# ------------------------------------------------------------------------------------------- #

# add items using list methods

# .append(item) - add the single item to the end of the list
fruits.append('lemon')
# print(fruits) # ['lime', 'banana', 'orange', 'lemon']

# .insert(index, item) - add the item at the index
fruits.insert(0, 'strawberry')
# print(fruits) # ['strawberry', 'lime', 'banana', 'orange', 'lemon']

# .extend(sequence) - add the items from the sequence to the end of the list
fruits.extend(['banana', 'guava', 'mango'])
# print(fruits) # ['strawberry', 'lime', 'banana', 'orange', 'lemon', 'banana', 'guava', 'mango']

# -------------------------------------------------------------------------------------------- #

# .append() is for single items, .extend is for multiple items
# fruits.append(['peach', 'plum']) # adds the whole list as a single item

# fruits.extend('watermelon') # adds each individual character to the list

# ----------------------------------------------------------------------------------------------- #

# remove items using list methods

# .remove(item) - remove the first occurrence of the item from the list
fruits.remove('banana')
# print(fruits) # ['strawberry', 'lime', 'orange', 'lemon', 'banana', 'guava', 'mango']


# .pop(index) - return the item at the index and return it. index defaults to -1 if not provided
# removed_fruit = fruits.pop() # remove the last item
# print(removed_fruit, fruits) # mango ['strawberry', 'lime', 'orange', 'lemon', 'banana', 'guava']

# fruits.pop(1) # remove the item at index 1
# print(fruits) # ['strawberry', 'orange', 'lemon', 'banana', 'guava']

# ------------------------------------------------------------------------------------------- #

# .index(item) - return the index of the item if it exists
# print(fruits.index('guava')) # 4
# print(fruits[4]) # guava

# item must exist to find its index
# fruits.index('kiwi') # ValueError: 'kiwi' is not in list

# ------------------------------------------------------------------------------------------ #

# .sort() - sort a list (of only strings or only numbers) in ascending order in place (returns None)
fruits.sort()
# print(fruits) # ['banana', 'guava', 'lemon', 'lime', 'mango', 'orange', 'strawberry']

numbers = [43, 24, 12, 79]
numbers.sort()
# print(numbers) # [12, 24, 43, 79]

# use reverse=True to sort in descending order
fruits.sort(reverse=True)
# print(fruits) # ['strawberry', 'orange', 'mango', 'lime', 'lemon', 'guava', 'banana']

# ------------------------------------------------------------------------------------------- #

# random.shuffle(list) - randomize a list
# random.shuffle(fruits)
# print(fruits) # ['mango', 'lime', 'orange', 'guava', 'lemon', 'strawberry', 'banana']

# ---------------------------------------------------------------------------------------------- #

# typecast to a list
# list(sequence) - return the sequence as list

# print(list('ABC')) # ['A', 'B', 'C']

# must use a sequence with list()
# list(123) # TypeError: 'int' object is not iterable

letters = list(letters)
# print(letters) # ['A', 'B', 'C', 'D', 'E', 'F', 'G']

# ------------------------------------------------------------------------------------------------- #

# string methods dealing with lists

# .split(separator) - split the string into a list at each instance of the separator string
letters = 'A-B-C'.split('-')
# print(letters) # ['A', 'B', 'C']

# split the string at each space
# print('red green blue'.split(' ')) # ['red', 'green', 'blue']

# glue_string.join(list) - join all the characters in the list into a string
#                          by placing the glue_string between each

# print(''.join(letters)) # ABC - join with blank string
# print(', '.join(letters)) # A, B, C - join with comma & space
# print(' _-^-_ '.join(letters)) # A _-^-_ B _-^-_ C

# ----------------------------------------------------------------------------------------- #

# 'nested' lists

grid = [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']]

grid = [
    ['O', 'O', 'X'],
    ['O', 'O', 'O'],
    ['O', 'O', 'O'],
]

# print(grid[0]) # ['O', 'O', 'X']
# print(grid[0][2]) # 'X'

grid[1][1] = 'X'

# print(grid) # [['O', 'O', 'X'], ['O', 'X', 'O'], ['O', 'O', 'O']]

'''
for row in grid:
    print(row)
'''

'''
['O', 'O', 'X']
['O', 'X', 'O']
['O', 'O', 'O']
'''

# ------------------------------------------------------------------------------------------ #

# for item in sequence - loop through each item of a sequence
'''
for fruit in fruits:
    print(fruit)
'''

# ------------------------------------------------------------------------------------------ #
'''
for fruit in fruits:
    # print only the fruits whose names are longer than 5 characters
    if len(fruit) > 5:
        print(fruit)

    else:
        print('...')
        
'''

# -------------------------------------------------------------------------------------- #

# for x in range() - loop a certain number of times

# range(stop) - return a range of numbers from 0 to stop-1
# print(list(range(5))) # [0, 1, 2, 3, 4]
'''
for x in range(10):
    print('*' * x)
'''

# --------------------------------------------------------------------------------------- #

# range(start, stop)
'''
for x in range(10, 21): # loop 10 - 20
    print(x)
'''

# ----------------------------------------------------------------------------------------- #

# range(start, stop, step)
'''
for x in range(0, 11, 2): # count from 0 to 10 by 2s
    print(x)
'''

# ------------------------------------------------------------------------------------------ #

# print(len(fruits)) # 7
'''
for index in range(len(fruits)):
    print(index, fruits[index])
'''

# ---------------------------------------------------------------------------------------------------- #

# nested loops
'''
for fruit_name in fruits:
    print(fruit_name)

    for letter in fruit_name:
        print(letter)

    print() # print a blank line
'''
