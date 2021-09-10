'''
Programming 102
Unit 1
'''

'''
Anatomy of an Error Message
----------------------------


Traceback (most recent call last):
  File "<FILENAME>.py", line number (approx)
    troublesome code (approx)
                   ^

ErrorType: specific error message
'''

# SyntaxError - a piece of code is missing or misplaced
# 4 + # SyntaxError - invalid syntax

# 'hello # (missing closing quote) SyntaxError: EOL (end of line) while scanning string literal

# print('hello world' # SyntaxError: unexpected EOF (end of file) while parsing

'''
print('hello world'

x = 9 # says the error comes from here
y = 10 # error moves here after line 28 is commnted, which means error is above
'''

# ------------------------------------------------------------------------------------------ #

# NameError - variable or function name was used that isn't defined
# xylophone # NameError: name 'xylophone' is not defined
# imaginary_function() # NameError: name 'imaginary_function' is not defined
# typE() # NameError: name 'typE' is not defined

# ------------------------------------------------------------------------------------------ #


# IndentationError - inconsistent horizontal placement

# "unexpected indent" - too far right
# "unindent does not match any outer indentation level" - too far left


'''
 x = 5 # IndentationError: unexpected indent

# -------- # 

x = 5
if x < 10:
    print("hello world")
     print("hello world") # IndentationError: unexpected indent
   print("hello world") # IndentationError: unindent does not match any outer indentation level

# -------- #

for x in range(10):
    # blank code block

print(x) # IndentationError: expected an indented block
'''

