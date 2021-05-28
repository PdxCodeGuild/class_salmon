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
index = linear_search(nums, 8)
print(index) # 7


# Part 2 - Binary Search
# Implement binary search, which requires that a list is sorted and divides its search range in half each iteration until it finds its target.
def binary_search(nums, value):
    low = nums[0]
    high = nums[-1]
    while low < high:
        mid = math.floor((low + high) / 2)
        if nums[mid] < value:
            low = mid + 1
        elif nums[mid] > value:
            high = mid - 1
        else:
            return mid
    return -1

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
index = binary_search(nums, 7) # returns -1 for values of 1 and 2
print(index) 


# Part 3 - Bubble Sort
# Bubble sort is one of the simplest and least efficient sorting algorithms. We repeatedly loop over the list, comparing each number to the one next to it, and swapping them if needed.
def bubble_sort(nums):
    length = len(nums)

#     procedure bubbleSort(A : list of sortable items)
#     n := length(A)
#     repeat
#         swapped = false
#         for i := 1 to n - 1 inclusive do
#             /* if this pair is out of order */
#             if A[i - 1] > A[i] then
#                 /* swap them and remember something changed */
#                 swap(A[i - 1], A[i])
#                 swapped := true
#             end if
#         end for
#     until not swapped
# end procedure