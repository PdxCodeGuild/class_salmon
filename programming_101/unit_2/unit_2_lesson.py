'''
Programming 101
Unit 2
'''

'''
Variables

- are used to store data that the program will use later
- can store ANY datatype
- BECOME the datatype they store
- can be given new values (be 'redefined')
'''

# = is the "assignment operator"
# it assigns the value on the right to the variable on the left

# assign the string 'purple' to the variable 'color'
color = 'purple'
# print(color) # purple

# ----------------------------------------------------------------- #

# variable 'color' IS a string because it CONTAINS a string
# print(type(color)) # <class 'str'>

# since 'color' contains a string, string operations can be performed using it
# print(color.upper()) # PURPLE

# change the value within 'color'
color = 'blue'
# print(color) # blue

# change the value within 'color' to the return value of .upper()
color = color.upper()
# print(color) # BLUE

# ------------------------------------------------------------------------------------ #

first_name = "Keegan"

# concatenate the values within the variables
output = "My name is " + first_name + '. My favorite color is ' + color.lower() + '.'
# print(output) # My name is Keegan. My favorite color is blue.

# ---------------------------------------------------------------- #

'''
Python Variable Names

- must start with a letter or underscore character
- cannot start with a number
- can only contain alphanumeric characters and underscores (A-z, 0-9, and _)
- are case sensitive (age, Age, AGE are 3 different variables)
'''

# python_variable_and_function_names_use_snake_case
# all lowercase words, separated with underscores

# variable names should seek to describe the data they contain

# -------------------------------------------------------------------------------------- #

# Valid variable names
username = "Athena" # ideal variable name format (all lowercase)
user_name = "Dionysus" # ideal variable name format (snake_case)
user_name_2 = "Artemis"
_username = "Aphrodite"
UserName = "Poseidon"
USERNAME = "Hera"

# --------------------------------------------------------------------------------------- #

# Invalid Variable Names
# 2username = "Nyx" # cannot start with a number
# user-name = "Hades" # no hyphens
# u$ern@me = "Cerberus" # no special characters other than underscores
# user name = "Persephone" # no spaces

# ----------------------------------------------------------------------------------------- #

# thisIsCamelCase (not used in Python)
# ThisIsTitleOrPascalCase
# ALLCAPS
# this-is-kebob-case

# ---------------------------------------------------------------------------------------- #


city = "Portland"
temp = 55

# concatenation only works between strings
# other datatypes will need to be "typecast" as string using str()
# str(object) - return a string representation of the object

output = "Welcome to " + city + "! Today the temperature is " + str(temp) + ' degrees.'

# f-string
# 'f' stands for 'formatted'.
# begin with an 'f' before the opening quote
# and allow Python expressions to be placed within the string using curly brackets {}

# f-strings don't care about datatype.
output = f"Welcome to {city}! Today the temperature is {temp} degrees."
# print(output)

# --------------------------------------------------------------------------------------- #

'''
user_string = input(prompt_message)

Print the prompt message and wait for the user to hit enter.
Once the user hits enter, anything they typed in the terminal will be returned.
The returned string can be saved in a variable such as 'user_string' above.

color = input('Enter a color: ')
print(f'My favorite color: {color}')
'''

# ------------------------------------------------------------------------------------- #

"""
# input() always returns a string

number = input('Please enter a number: ')

print(number, type(number)) # 5 <class 'str'>
print(number + number) # '55'

# typecasting functions
# str(object) - return a string representation of the object, if possible
# int(object) - return an integer representation of the object, if possible
# float(object) - return a float representation of the object, if possible

# integer 'int' - whole numbers
# float 'float' - decimal numbers

# convert the string version of the number to a float
# and save the float version over the original
number = float(number)

print(number, type(number)) # 5.0 <class 'float'>
print(number + number) # 10.0
"""

# ------------------------------------------------------------------------------------ #
'''
# find the area of a rectangle with user defined sides

# have the user define the height and width of the rectangle
height = input("Please enter the height of the rectangle: ")
width = input("Please enter the width of the rectangle: ")

# convert the height and width to float values
height = float(height)
width = float(width)

# calculate the area of the rectangle
area = height * width # asterisk is multiplication

# display the results
result = f"""
Area of a Rectangle
-------------------
height ... {height}
width .... {width}

area ..... {area}
"""

print(result)

'''
# ----------------------------------------------------------------------------- #

x = 5
y = 3

# print(x + y)  # addition +
# print(x - y)  # subtraction -

# print(x * y)  # multiplication *
# print(x ** y) # exponentiation ** (x^y)

# print(x / y)  # 'regular' division / (result in a float)
# print(x // y) # 'floor' division // (always round down)

# print(x % y)  # modulus % (remainder after division)

# ----------------------------------------------------------------------------- #