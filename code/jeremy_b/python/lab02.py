"""

Author: Jeremy Bush
Project: Programming Boot Camp Lab 02
Version: 4
Date: 5/18/2021

"""


# Version 3 code
# Let user input everything in one input statement.
print("Enter integers to average.  Separate each with a comma.  Press enter when done.")
numbers_entered = input("Enter integers: ")

# find and replace any spaces in the string.
numbers_entered = numbers_entered.replace(" ", "")

# split string
numbers_entered = numbers_entered.split(",")

# Check for and remove any non-integer characters.
numbers_entered = [number for number in numbers_entered if number.isdigit()]  # more list comprehension

# convert values into integers.
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
