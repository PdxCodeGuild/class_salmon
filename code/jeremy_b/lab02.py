"""

Author: Jeremy Bush
Project: Programming Boot Camp Lab 02
Version: 1
Date: 5/18/2021

"""

# List of numbers
nums = [3, 4, 5]

# get the total sum of all values.
total = 0
for number in nums:
    total += number

# print the average of the numbers in the list.
print(f"Average: {int(total/len(nums))}")
