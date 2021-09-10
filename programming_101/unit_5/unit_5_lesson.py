'''
Programming 101
Unit 5
'''

import string
import random

letters = string.ascii_letters
# print(letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

digits = string.digits
# print(digits) # 0123456789

punctuation = string.punctuation
# print(punctuation) # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

# concatenate all the characters together into a giant string
all_characters = letters + digits + punctuation
# print(all_characters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

# ----------------------------------------------------------------------------------------------------------- #

# while loop

'''
while some_condition == True:
    # loop this code block
    # until some_condition
    # becomes False
'''

# for x in range(10):
x = 0

while x < 10:

    # print(x)

    # change the counter to eventually end the loop
    x += 1

# ----------------------------------------------------------------------------------- #

# string pattern builder - run a loop to create a pattern of string characters

# blank string to hold the pattern
pattern = ''

# loop will end when the string's length is greater than 10
while len(pattern) <= 10:

    # if the pattern's length is even
    if len(pattern) % 2 == 0:
        pattern += '*'

    # if the pattern's length is odd
    elif len(pattern) % 2 == 1:
        pattern += '-'

    # print(pattern) # print the string after each character is added

# print(pattern) # *-*-*-*-*-*

# --------------------------------------------------------------------------------- # 

numbers = []

# generate a list of 10 random integers between 1 and 100
while len(numbers) < 10:
    # add a random integer to the list
    numbers.append(random.randint(1, 100))

# print(numbers) # [22, 8, 25, 21, 48, 35, 7, 20, 48, 24]

# ------------------------------------------------------------------------------- #

# remove one number at a time from the list until the list is empty

# print(numbers)

# loop while the numbers list still has numbers in it
# while numbers: # same thing as 84 (truthy / falsey)
while numbers != []:
    # remove one item from the end
    number = numbers.pop()

    # print(number, numbers)

# ---------------------------------------------------------------------------- #


# loop controls
# else, break, continue

for x in range(10):

    # if x == 1 or x == 3 or x == 5 or x == 7:
    if x in [1, 3, 5, 7]: # same as line 98
        print('*' * x)
        continue # skip the rest of this iteration and begin the next

    if x == 8:
        print('Goodbye!')
        break # end the loop immediately

    print(x)

else:
    # if the loop's condition becomes False
    # else will be triggered
    print('The loop made it all the way to the end!')

