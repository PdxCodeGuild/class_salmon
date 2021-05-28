###################  Part 1   ####################
nums = [1, 2, 3, 4, 5, 6, 7, 8]


def linear_search(nums, value):
    for digit in nums:
        if digit == value:
            return (f'The number {value} is at index {nums.index(value)}')
    else:
        return "That number is not in this list."


index = linear_search(nums, 11)
print(index)

'''
###################  Part 2   ####################

nums = [1, 2, 3, 4, 5, 6, 7, 8]

def binary_search(list, target):
    my_list = list[:]
    my_list.sort()
    low_val = my_list[0]
    high_val = my_list[-1]
    mid = (low_val + high_val)//2

    while low_val < high_val:
        if mid == target:
            return (f'The {target} is at index {my_list.index(mid)}')
            break
        else:
            if target > mid:
                low_val = mid
                mid = (low_val + high_val)/2

            elif target < mid:
                high_val = mid
                mid = (low_val + high_val)/2
    else:
        return "That number is not in this list."



print(binary_search(nums, 0))

###################  Part 3   ####################

import time
import random
nums2 = [random.randint(0, 100000) for _ in range(100000)]
t1 = time.time()


nums = [1, 33, 2, 4, 7, 5, 6, 8, 2, 1]


def bubble_sort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-1):
            if nums[j] > nums[j+1]:
                smaller_num = nums.pop(j)
                nums.insert((j+1), smaller_num)

    return nums


t2 = time.time()

print(bubble_sort(nums), '\nTime: ', t2 - t1)
###################  Part 4   ####################
nums = [1, 33, 2, 4, 7, 5, 6, 8, 2, 1]
i = 1
while i < len(nums):
    j = i
    while j > 0 and nums[j-1] > nums[j]:
        smaller_num = nums.pop(j)
        nums.insert((j-1), smaller_num)
        j = j - 1
    i = i + 1
print(nums)

'''
###################  Part 5   ####################
## Lost in the  pseudocode   ###
nums = [1, 33, 2, 4, 7, 5, 6, 8, 2, 1]


def quicksort_recursive(nums, low, high):
    if low < high:
        p = partition
'''
