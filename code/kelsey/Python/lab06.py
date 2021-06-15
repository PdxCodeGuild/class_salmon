# Lab 6: Credit Card Validation
# Let's write a function which returns whether a string containing a credit card number is valid as a boolean. 

user_enters = input('Enter your credit card number: ')

def cc_valid(original_numbers):
    list_of_original_numbers = list(original_numbers)
# Convert the input string into a list of ints
# 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5
    list_of_ints = [int(num) for num in list_of_original_numbers]
# Slice off the last digit. That is the check digit.
# 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5  
    check_digit = list_of_ints.pop()
# Reverse the digits.
# 5 8 9 9 8 6 8 5 7 3 7 6 5 5 4
    reversed_digits = list(reversed(list_of_ints))
# Double every other element in the reversed list.
# 10 8 18 9 16 6 16 5 14 3 14 6 10 5 8 
    every_other_dbld = [digit * 2 if i % 2 == 0 else digit for i, digit in enumerate(reversed_digits)]
# Subtract nine from numbers over nine.
# 1 8 9 9 7 6 7 5 5 3 5 6 1 5 8
    subtract_nine = [digit - 9 if digit > 9 else digit for digit in every_other_dbld]
# Sum all values.
# 85
    digit_sum = sum(subtract_nine)
# Take the second digit of that sum.
# 5 
    second_digit = digit_sum % 10
# If that matches the check digit, the whole card number is valid.
# Valid!
    return second_digit == check_digit


if cc_valid(user_enters) == True:
    print('Valid!')
else:
    print('Invalid')

