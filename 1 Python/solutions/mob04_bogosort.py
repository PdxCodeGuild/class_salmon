
import random
import time

# Lab: Bogo Sort
# Bogo sort is one of the least efficient sorting algorithms imaginable! It works by generating random arrangements of a list, checking if the list is sorted, and if it is, return it. For a list of 200 numbers, there are 200! = 7.88*10^374 possible combinations, only one of them is the sorted list.

# random_list(n) generates and returns a list of length n, with random values between 0 and 100

def random_list(n):
    output = []
    for i in range(n):
        output.append(random.randint(1, 99))
    return output

# shuffle(nums) randomly re-arranges a list

# iterate through the indices of the list
# for each index, generate a random index
# swap the elements at the two indices


# indices: 0   1   2   3   4  5  6
# values:  62, 57, 13, 17, 7, 3, 59

# i = 0, j = 5
# indices: i                  j
# values:  62, 57, 13, 17, 7, 3, 59

# i = 1, j = 2
# indices:    i   j          
# values:  3, 57, 13, 17, 7, 62, 59

# i = 2, j = 6
# indices:        i              j
# values:  3, 13, 57, 17, 7, 62, 59

# i = 2
# indices:        
# values:  3, 13, 59, 17, 7, 62, 57


# def get_size():
#     return 8, 12 # tuple packing
# size = get_size()
# print(size)
# width, height = get_size() # tuple unpacking
# print(width)
# print(height)




# https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle

def shuffle(nums):
    for i in range(len(nums)):
        j = random.randint(0, len(nums)-1)

        # k = nums[i]
        # nums[i] = nums[j]
        # nums[j] = k

        nums[i], nums[j] = nums[j], nums[i]




# is_sorted(nums) checks if a list is sorted
# iterate through the indices of the list
# if the element at the current index is greater than the element at the next index, the list isn't sorted, and you can return False
# if you get through the entire list and each element is less than or equal to the next element, the list is sorted, and you can return True



# i
# 1 2 3 4 5
# 2 < 1 - good

#   i
# 1 2 3 4 5
# 2 < 3 - good

#     i
# 1 2 3 4 5
# 3 < 4 - good

#       i
# 1 2 3 4 5
# 4 < 5 - good

# sorted!

# 1 2 3 4 3 - not sorted

def is_sorted(nums):
    for i in range(len(nums)-1):
        if nums[i] <= nums[i+1]:
            if i == len(nums)-2:
                return True
        else:
            return False

    # for i in range(len(nums)-1):
    #     if nums[i] > nums[i+1]:
    #         return False
    # return True


# bogosort(nums) continues to rearrange the list until the list is sorted
def bogosort(nums):
    counter = 0
    start_time = time.time()
    while is_sorted(nums) == False:
        shuffle(nums)
        counter += 1
    end_time = time.time()
    total_time = end_time - start_time
    print(f'Time elapsed: {total_time} seconds')
    print(f'Steps taken: {counter}')
    print(f'Time per step: {total_time/counter} seconds')
    

# print(is_sorted([1, 2, 3, 4, 5])) # True
# print(is_sorted([1, 2, 3, 4, 3])) # False


# n! = n*(n-1)*(n-2)*...*1
# 6! = 6*5*4*3*2*1 = 720

# to bogosort a list of 100 numbers
# 100! * 8.342550007615607e-06 / 60 / 60 / 24 / 365 / (13.8 billion)
# = 1.789027e+135 times the age of the universe


nums = random_list(10) # create a new list
print(nums) # initial list
bogosort(nums) # sort the list
print(nums) # sorted list



