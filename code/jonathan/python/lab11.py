import random

def linear_search(nums, value):
    for num in nums:
        # counter
        computations = 0
        if num == value:
            computations += 1
            return (nums.index(value))
        
def binary_search(a, b, c):
    low = 0
    high = len(nums)
    while low < high:
        mid = ((low + high) // 2)
        if value < nums[mid]:
            # make high equal to mid and loop
            high = mid
        elif value > nums[mid]:
            # make low equal to mid and loop
            low = mid
        else:
            return (nums.index(value))
    return None

def bubble_sort(a):
    swapped = True
    length = len(random_nums)
    while swapped != False:
        swapped = True
        for i in range(len(random_nums) - 1):
            for j in range(0, length - i - 1):
                if random_nums[j] > random_nums[j + 1]:
                    random_nums[j], random_nums[j + 1] = random_nums[j + 1], random_nums[j] 
                    swapped = False
                    print(random_nums)

# list of numbers to work with            
nums = [1, 2, 3, 4, 5, 6, 7, 8]
# setting a target
value = 3
# for the bubble sort portion
random_nums = random.sample(range(0, 8), 8)

# index of target in list linear
linear_sort = linear_search(nums, 3)
# print
print(linear_sort)
# index of target in list binary
binary_sort = binary_search(nums, len(nums), value)
print(binary_sort)
bubbles = bubble_sort(random_nums)