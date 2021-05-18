"""

Author: Jeremy Bush
Project: Programming Boot Camp Lab 02
Version: 2
Date: 5/18/2021

"""

"""
This code was used for version 1.

# List of numbers
nums = [3, 4, 5]
"""

"""
# Version 2 code for obtaining input.
# Get user to input numbers.
nums = []
number_entered = ''
print("Enter integers to average.  Once numbers have been entered, enter 'done'.")
while True:
    number_entered = input("Enter an integer: ")
    if number_entered.lower() == 'done':
        break
    else:
        nums.append(int(number_entered))
"""

# Version 3 code
# Let user input everything in one input statement.
print("Enter integers to average.  Separate each with a comma.  Press enter when done.")
numbers_entered = input("Enter integers: ")

# find and replace any spaces in the string.
numbers_entered = numbers_entered.replace(" ", "")

# split string and convert values into integers.
numbers_entered = numbers_entered.split(",")
nums = [int(number) for number in numbers_entered]  # Conversion via list comprehension.


# get the total sum of all values.
total = 0
for number in nums:
    total += number

# print the average of the numbers in the list.  If average has no remainder, print as int.
if total % len(nums) == 0:
    print(f"Average: {int(total/len(nums))}")
else:
    print(f"Average: {total/len(nums):.2f}")
