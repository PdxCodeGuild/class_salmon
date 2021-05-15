


import random

# O(1)
def random_element(nums):
    index = random.randint(0, len(nums)-1)
    return nums[index]
print(random_element([1, 2, 3, 4])) # 4

# O(n)
def calculate_total(nums):
    total = 0
    for num in nums:
        total += num
    return total
print(calculate_total([1, 2, 3, 4])) # 10

# O(n^2)
def find_pair(nums, target):
    output = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and nums[i] + nums[j] == target:
                output.append((nums[i], nums[j]))
    return output

print(find_pair([5, 6, 2, 3, 4], 7)) # [5, 2]

