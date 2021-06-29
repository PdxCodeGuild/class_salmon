import math
def linear_search(nums, value):
    for i, num in enumerate(nums):
        if num == value:
            return i
    return 'Value not found!!!!'
# index 0  1  2  3  4  5  6  7
nums = [1, 2, 3, 4, 5, 6, 7, 8]
index = linear_search(nums, 3)
print(index) # 2

def binary_search(nums, value):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = math.floor((low + high) / 2)
        if nums[mid] < value:
            low = mid +1
        elif nums[mid] > value:
            high = mid - 1
        else:
            return mid
    return 'Unsuccessful'
#       0  1  2  3  4  5  6  7
nums = [1, 2, 3, 4, 5, 6, 7, 8]
index = binary_search(nums, 3)
print(index) # 2

def bubble_sort(nums):
#procedure bubbleSort(A : list of sortable items)
    n = len(nums)
    for i in range(n-1):
        swapped = False
        for i2 in range(n - 1) :
            if nums[i2] > nums[i2+ 1] : 
                temp = nums[i2]
                nums[i2] = nums[i2 + 1]
                nums[i2 + 1] = temp
                swapped =True
        if swapped == False:
            break

    return nums 

#       0  1  2  3  4  5  6  7
print(bubble_sort([4,6,1,3]))