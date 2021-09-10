import random # imports 880 lines of code into a single variable
import string # imports 280 lines of code

letters = string.ascii_uppercase
random_number = random.randint(1, 100)
random_letter = random.choice(letters)

# print(random_number, random_letter, letters)

# -------------------------------------------------------------------------- #

# import specific attributes from a module
# keywords: from, import

from string import ascii_uppercase # imports 1 line instead of 280
from random import randint, choice # import only randint() and choice()

# dot notation is no longer needed to access the imported attributes
letters = ascii_uppercase # shorten the variable name
random_number = randint(1, 100)
random_letter = choice(letters)

# print(random_number, random_letter, letters)

# ----------------------------------------------------------------- # 

# import specific attributes from a module and change their variable name
# keywords: from, import, as

from string import ascii_uppercase as letters
from random import randint as r_int, choice as r_choice

random_number = r_int(1, 100)
random_letter = r_choice(letters)

# print(random_number, random_letter, letters)

# ------------------------------------------------------------------ #


