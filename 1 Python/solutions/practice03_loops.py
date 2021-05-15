




# Practice 3: While and For Loops
# Copy and paste this file into your own "03_loops.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 03_loops.py"

# Double Numbers
# Write a function that takes a list of numbers and returns a new list with every number doubled

def double_numbers(nums):
    for i in range(len(nums)):
        nums[i] *= 2
    # return nums

def double_numbers2(nums):
    output = []
    for num in nums:
        output.append(num*2)
    return output


def double_numbers3(nums):
    nums = nums.copy()
    for i in range(len(nums)):
        nums[i] *= 2
    return nums

#                     0   1   2
# print(double_numbers([50, 12, 99])) # [100, 24, 198]

# nums = [50, 12, 99]
# double_numbers(nums)
# print(nums)

# import random
# random.shuffle(nums)



# nums = [50, 12, 99]
# output = double_numbers(nums)
# print(output)
# print(nums)


# fruits = ['apples', 'bananas', 'pears']
# fruits2 = fruits
# fruits2 = ['a', 'b', 'c']
# print(fruits)


def test_double_numbers():
    assert double_numbers2([1, 2, 3]) == [2, 4, 6]


# Stars
# Write a function that takes an integer and returns that number of asterisks in a string

def stars(n):

    # return '*'*n

    output = ''
    for stars in range(n):
        output += '*'
    return output


# print(stars(4)) # ****



def test_stars():
    assert stars(1) == '*'
    assert stars(2) == '**'
    assert stars(3) == '***'
    assert stars(4) == '****'


# Extract Less Than Ten
# Write a function to move all the elements of a list with value less than 10 to a new list and return it.

def extract_less_than_ten(nums):
    below_ten = []
    for digit in nums:
        if digit < 10:
            below_ten.append(digit)
    return below_ten

def test_extract_less_than_ten():
    assert extract_less_than_ten([2, 8, 12, 18]) == [2, 8]


# Factorial
# Write a function that takes `n` as a parameter and returns `n` factorial.
# 5! = 5*4*3*2*1 = 120
# 8! = 8*7*6*5*4*3*2*1 = 40320

def factorial(n):

    # start an output value at 0
    # loop n times
        # adding output value to previous output value
    
    # output = 1
    # while n > 1:
    #     output *= n
    #     n -= 1
    # return output

    output = n
    while n > 2:
        n -= 1
        output *= n
    return output

    # output = 1
    # for i in range(2, n+1):
    #     output *= i
    # return output

# print(factorial(5)) # 120
# print(factorial(8)) # 40320


# Fibonacci
# Write a function that takes `n` as a parameter, and returns a list containing the first `n` [Fibonacci Numbers](https://en.wikipedia.org/wiki/Fibonacci_number).

def fibonacci(n):
    num1 = 0
    num2 = 1
    output = [num1, num2]
    for count in range(n-2):
        total = num1 + num2
        output.append(total)
        num1 = num2
        num2 = total
    return output

    # output = [0, 1]
    # for count in range(n-2):
    #     output.append(output[-1] + output[-2])
    # return output

#                      num1 num2  total
# print(fibonacci(10)) # [0,   1,    1,   2,    3,    5,    8,    13,    21,    34]

