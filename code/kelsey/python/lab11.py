# Lab 11: Searching and Sorting

import math

# Part 1 - Linear Search
# Implement linear search, which simply loops through the given list and check if each element is equal to the value we're searching for. If it is, return the index at which it was found, otherwise, return a value indicating that it was not found.
def linear_search(nums, value):
    for index, num in enumerate(nums):
        if num == value:
            return index
    return -1    

nums = [1, 2, 3, 4, 5, 6, 7, 8]
print(linear_search(nums, 5)) # index = 4


# Part 2 - Binary Search
# Implement binary search, which requires that a list is sorted and divides its search range in half each iteration until it finds its target.
def binary_search(nums, value):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = math.floor((low + high) / 2)
        if nums[mid] < value:
            low = mid + 1
            print(mid, low)
        elif nums[mid] > value:
            high = mid -1
            print(mid, high)
        else:
            return mid
    return -1

nums = [1, 2, 3, 4, 5, 6, 7, 8]
print(binary_search(nums, 4)) # index = 3


# Part 3 - Bubble Sort
# Bubble sort is one of the simplest and least efficient sorting algorithms. We repeatedly loop over the list, comparing each number to the one next to it, and swapping them if needed.
def bubble_sort(nums):
    swapped = True
    while swapped == True:
        swapped = False
        for i in range(1, len(nums)):
            num_1 = nums[i-1]
            num_2 = nums[i]
            if nums[i - 1] > nums[i]:
                nums[i] = num_1
                nums[i-1] = num_2
                swapped = True


nums = [9, 3, 46, 1, 77, 33, 5]
bubble_sort(nums)
print(nums) # [1, 3, 5, 9, 33, 46, 77]

