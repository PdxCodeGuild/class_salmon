'''
Programming 101
Unit 1 Review
'''

# Welcome to PDX Code Guild
# single-line comments use pound sign #
# everything to the right of the # is a comment

"""
Multi-line
comment with
double quotes
"""

'''
Multi-line
comment with
single quotes
'''

"""
Comments

organize code
explain code
exclude lines of code for testing
"""

# -------------------------------------------------------------------------------- #

# a function is a named piece of code that performs a specific task

# print(data) - display the data in the terminal

# functions need parentheses after their name in order to be executed
# print 'hello' # SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello')?

# print('hello') # hello
# print() # print a blank line
# print('world') # world

# multiple, comma-separated items will be printed with a space between each
# print('pi:', 3.141592654) # pi: 3.141592654
# print('a', 'b', 'c') # a b c

# -------------------------------------------------------------------------------- #

# datatype: string (str)

# strings are sequence of textual characters surrounded by quotes

'cat'
"213456789"
'$%^&*'
"...entire contents of a book..."

'' # blank string
"" # blank string

# ------------------------------------------------------------------------------ #

# type(object) - return the datatype of the object
# everything in Python is an object

# print(type('')) # <class 'str'>
# print(type('12345')) # <class 'str'>

# ------------------------------------------------------------------------------- #
"""

# print a multi-line string
print('''
Multi-line comments
    are also
        multi-line strings
''')

"""
# ----------------------------------------------------------------------------- #

# Concatenation - adding strings together to form a single string

# print('pdx' + 'code' + 'guild') # pdxcodeguild
# print('pdx' + ' ' + 'code' + ' ' + 'guild') # pdx code guild

# ----------------------------------------------------------------------------- #

# string methods

# a "method" is a function that manipulates only the object to which it belongs
# an object's methods are accessed with a dot . after the object

# .upper() - return an uppercase version of the string
# print('abc'.upper()) # ABC

# .lower() - return a lowercase version of the string
# print('XYZ'.lower()) # xyz

# .replace(old, new) - replace the old string with the new string
# print('hello'.replace('h', 'j')) # jello

# ----------------------------------------------------------------------------- #

# parentheses are required on method call
# OOPS! forgot parentheses on the method call
# print('abc'.upper) # <built-in method upper of str object at 0x000002010DDFB770>

# ------------------------------------------------------------------------------- #

# Escape Characters
# denoted with a backslash before the character \
# allow characters to "escape" the normal rules of Python strings

# "hello "world"" # Error! Quotes cancel each other
# 'I don't like spam!' # Error! Quotes cancel each other

# print using mismatched quote sets
# print('hello "world"') # hello "world"
# print("I don't like spam!") # I don't like spam!

# print using escape characters
# print("hello \"world\"") # hello "world" - use the \" escape character to place double quotes within the string
# print('I don\'t like spam!') # I don't like spam! - use the \' escape character

# print("\"") # print a double quote
# print("\\") # print a backslash

# formatting strings with escape characters
# print("A\nB\nC") # \n - new line character
# print("A\tB\tC") # \t - horizontal tab character

# ------------------------------------------------------------------------------------ #