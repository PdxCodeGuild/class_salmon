# Lab 6: Credit Card Validation
# Let's write a function which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:

# Convert the input string into a list of ints

'''
user inputs 16 numbers into empty list (while loop)
convert list of strings into integers
Slice off the last digit. That is the check digit (???) will work for 15
reverse list .reverse()

list comprehensions
don't have to do steps in order 




'''
user_input = []

while True:
    user_enters = input('Please enter credit card number: ')
    i = 0
    for n in user_input:
        i += n
        print(user_input)
        break
    else:
        user_input = user_enters
        user_input.append(user_enters)
        

cc_numbers = [num for num in cc_numbers in range(16)]

# 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5

# Slice off the last digit. That is the check digit.
# 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5

# Reverse the digits.
# 5 8 9 9 8 6 8 5 7 3 7 6 5 5 4

# Double every other element in the reversed list.
# 10 8 18 9 16 6 16 5 14 3 14 6 10 5 8

# Subtract nine from numbers over nine.
# 1 8 9 9 7 6 7 5 5 3 5 6 1 5 8

# Sum all values.
# 85

# Take the second digit of that sum.
# 5

# If that matches the check digit, the whole card number is valid.
# Valid!