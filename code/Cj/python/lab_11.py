import random

nums = [1, 2, 3, 4, 5, 6, 7, 8]

def linear_search(nums, value):
    for i, val in enumerate(nums):
        if val == value:
            return i
    return "Not found."

# index = linear_search(nums, 5)
# print(index)

def binary_search(location, value):
    location.sort()
    flagged = False
    low = 0
    high = len(location) -1
    while low <= high and not flagged: 
        mid = (low+high)//2    
        if value == location[mid]:
            flagged = True
        elif value > location[mid]:
            low = mid+1
        else:
            high = mid -1
    if flagged == True:
        return mid
    else:
        return 'Value not found.'

# x = binary_search(nums, 6)
# print(x)

def bubble_sort(parameter):
    length = len(parameter)-1
    swapped= True
    while swapped:
        swapped = False
        for i in range(len(parameter)-1):
            if parameter[i] > parameter[i+1]:
                swapped = True
                parameter[i], parameter[i+1] = parameter[i+1], parameter[i]
    return parameter

print(bubble_sort([5, 4, 7, 2, 9, 7, 9, 6, 8, 3]))
