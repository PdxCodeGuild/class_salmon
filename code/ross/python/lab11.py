def linear_search(nums, value):
  for i in nums:
      if nums[i] == value:
          return i

# index 0  1  2  3  4  5  6  7
nums = [1, 2, 3, 4, 5, 6, 7, 8]
index = linear_search(nums, 3)
print(index) # 2

# ----------- BINARY SEARCH -------------
def binary_search(nums, value):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] < value:
            low = mid + 1
        elif nums[mid] > value:
            high = mid - 1
        else:
            return mid
    return "Could not locate the target value in the list"
#       0  1  2  3  4  5  6  7
nums = [1, 2, 3, 4, 5, 6, 7, 8]
index = linear_search(nums, 3)
print(index) # 2

# ------------------ BUBBLE SORT ----------------------
def bubbleSort(nums):
    length = len(nums)
    swapped = False
    # while swapped == False:
    for j in range(length):
        for i, num in enumerate(nums):
            # print(nums)
            try:
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    # print(nums)
                elif nums[i] < nums[i + 1]:
                    pass
            except IndexError:
                break
    return nums
    # return swapped
'''    for j in range(length):
        for i, num in enumerate(nums):
            print("i", i, "num", num)
            print(nums)
            try:
                if nums[i] > nums[i + 1]:
                    temp = nums[i]
                    nums[i] = nums[i + 1]
                    nums[i + 1] = temp
                    print(nums)
                elif nums[i] < nums[i + 1]:
                    break
            except IndexError:
                pass'''

#       0  1  2  3  4  5  6  7
nums = [8, 6, 5, 4, 3, 2, 1, 7] # pass it a list of unsorted numbers
print(bubbleSort(nums)) # should be sorted list