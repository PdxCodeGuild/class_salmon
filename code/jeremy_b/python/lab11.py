"""

Author: Jeremy Bush
Project: Programming Boot Camp Lab 08
Version: 1
Date: 5/24/2021

"""


import random


def linear_search(nums, to_find):
    for num in nums:
        if to_find == num:
            return nums.index(num)
    return -1


def binary_search(nums, to_find):
    low = 0
    mid = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if mid < to_find:
            low = mid + 1
        elif mid > to_find:
            high = mid - 1
        else:
            return nums.index(mid)
    return -1


def bubble_sort(nums):

    for i in range(len(nums) - 1):
        for j in range(0, len(nums) - 1 - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j+1], nums[j]
    return nums


# Linear search:
sample = [1, 2, 3, 4, 5, 6, 7, 8]
number = int(input("Enter an integer: "))
index = linear_search(sample, number)
if index == -1:
    print("Number was not found.")
else:
    print(index)

# Binary search
number = int(input("Enter an integer: "))
index = binary_search(sample, number)
if index == -1:
    print("Number was not found.")
else:
    print(index)

# bubble search
sample = [random.randint(1, 100) for i in range(20)]
print(f"Original List: {sample}")
print(f"  Sorted List: {bubble_sort(sample)}")
