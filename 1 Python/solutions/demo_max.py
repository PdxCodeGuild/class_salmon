





def max(nums):
    running_max = nums[0]
    for num in nums:
        if num > running_max:
            running_max = num
    return running_max


# print(max([56, 105, 21, 32, 64])) # 105


# 5! = 5*4*3*2*1
# 8! = 8*7*6*5*4*3*2*1

def factorial(n):
    output = 1
    for i in range(1, n+1):
        output *= i
    return output

# print(factorial(5))


def factorial_recursive(n):
    if n == 1:
        return 1
    return n*factorial_recursive(n-1)

# print(factorial_recursive(5))


def binary_search(nums, target):
    low = 0
    high = len(nums)-1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return None

print(binary_search([5, 6, 7, 8], 7)) # 2



def binary_search_recursive(nums, target, low, high):
    if low > high:
        return None
    mid = (low + high) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binary_search_recursive(nums, target, mid+1, high)
    else:
        return binary_search_recursive(nums, target, low, mid-1)
    
print(binary_search_recursive([5, 6, 7, 8], 7, 0, 3)) # 2



def fibonacci(n):
    nums = [0, 1]
    for i in range(n-2):
        nums.append(nums[-1] + nums[-2])
    return nums[-1]

print(fibonacci(7)) # 8


def fibonacci_recursive(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

print(fibonacci_recursive(7)) # 8