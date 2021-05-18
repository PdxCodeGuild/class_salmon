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

# get the total sum of all values.
total = 0
for number in nums:
    total += number

# print the average of the numbers in the list.
print(f"Average: {int(total/len(nums))}")
