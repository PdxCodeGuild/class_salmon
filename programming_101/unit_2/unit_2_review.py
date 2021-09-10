'''
Programming 101
Unit 2 Review
'''

# variables are named storage spaces

# assign a value to a variable using =
fruit = 'apple' # assign the string 'apple' to the variable 'fruit'
# print(fruit) # apple

# --------------------------------------------------------------------------------- #

# variables become the datatype they store
# type(object) - return the datatype of the object

fruit_datatype = type(fruit)
# print(fruit, fruit_datatype) # apple <class 'str'>

# ----------------------------------------------------------------------------------- #

# change the value within the variable
fruit = 'orange'
# print(fruit) # orange

# call a string method and overwrite the variable with the result
fruit = fruit.upper()
# print(fruit) # ORANGE

# concatenate using the string within the variable
message = "Favorite fruit: " + fruit.title()
# print(message) # Favorite fruit: Orange

# ----------------------------------------------------------------------------------- #

# beware of using Python keywords as variables
# print = 'Hello world' # replaces the print function with the string 'Hello world'
# print('abc') # Error! print function no longer exists

# ------------------------------------------------------------------------------------ #

'''
Python Variable Names

- must start with a letter or underscore
- cannot start with a number
- can only contain alphanumeric characters and underscores (A-z, 0-9, and _)
- are case sensitive (age, Age, AGE are 3 different variables)
'''

# python_variable_and_function_names_use_snake_case
# all lowercase words separated with underscores

# ThisIsTitleOrPascalCase - used in Python for defining classes
# ALLCAPS - generally used for constant variables

# ----------------------------------------------------------------------------------------- #

# f-strings
# 'f' stands for 'formatted'.
# Begin with a 'f' before the opening quote
# Python expressions (code) can be placed within the string using curly brackets {}

number = 99.5

# concatenation only works between strings.
# other datatypes will need to be "typecast" as strings using str()
output = "The number is " + str(number)

# f-string's don't care about datatype
output = f"The number is {number}"
# print(output) # The number is 99.5

# ------------------------------------------------------------------------------------------- #

# input() - allows the user to interact with the code
'''
user_string = input(prompt_message)

Print the prompt_message and wait for the user to hit 'enter'.
Once the user hits enter, anything they typed in the terminal will be returned.
The return value can be captured in a variable and used in the code

fruit = input("Enter a fruit: ")
print(f"Favorite fruit: {fruit}")
'''

# ------------------------------------------------------------------------------------------------ #
'''
# input() always returns a string

number = input("Enter a number: ")

print(number, type(number)) # 5 <class 'str'>
print(number * 10) # 5555555555

# in order to use input() for numbers, the return value will need to be typecast as a number
# int(object) - return the object as an integer, if possible
# float(object) - return the object as an float, if possible

# override the number variable with a float version of itself
number = float(number)

print(number, type(number)) # 5.0 <class 'float'>
print(number * 10) # 50.0
'''
# ----------------------------------------------------------------------------------------- #

# values passed to int() and float() must LOOK like numbers
# int('fish') # ValueError: invalid literal for int() with base 10: 'fish'
# float('fish') # ValueError: could not convert string to float: 'fish'

# ------------------------------------------------------------------------------------------ #

x = 5
y = 3

# arithmetic operators

# print(x + y)  # addition +
# print(x - y)  # subtraction -
# print(x * y)  # multiplication *
# print(x ** y) # exponentiation ** (x^y)
# print(x / y)  # 'regular' division / (result in a float)
# print(x // y) # 'floor' division // (always round down to nearest integer)
# print(x % y)  # modulus % (remainder after division)

# -------------------------------------------------------------------------------- #

# print(89 // 25) # 3 - how many quarters are in 89 cents
# print(89 % 25) # 14 - how many cents are leftover after taking out the quarters

# -------------------------------------------------------------------------------- #

# % 2 can used to find even/odd
# print(84 % 2) # 0 - even
# print(85 % 2) # 1 - odd

# ----------------------------------------------------------------------------------- #

x = 3

x * 2 # uses x, but doesn't change it

# print(x * 2) # 6 - uses x, but doesn't change it
# print(x) # 3

# multiply x by 2 and save the result over the previous value of x
x = x * 2
# print(x) # 6

# ReAssignment Operators
x += 2  # x = x + 2
x -= 2  # x = x - 2
x *= 2  # x = x * 2
x **= 2 # x = x ** 2
x /= 2  # x = x / 2
x //= 2 # x = x // 2
x %= 2  # x = x % 2
