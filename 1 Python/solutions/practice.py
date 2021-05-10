import random

def is_even(a):
    """ returns if number is even

    >>> is_even(1)
    False
    >>> is_even(2)
    True
    """
    return a%2 == 0
    
    # # equivalent to above
    # if a%2 == 0:
    #     return True 
    # else: 
    #     return False


def opposite(a, b):
    """ returns if a and b have opposite polarity
    
    >>> opposite(1, -1)
    True
    >>> opposite(-1, 0)
    True
    >>> opposite(-1, -9)
    False
    >>> opposite(2, 3)
    False
    """
    return (a >= 0 and b < 0) or (a < 0 and b >= 0)
    
    # # equivalent to above
    # if (a > 0 and b < 0):
    #     return True  
    # elif (a < 0 and b > 0):
    #     return True 
    # else:
    #     return False


def double_letters(text):
    """
    returns the string text with each character doubled

    >>> double_letters('hello')
    'hheelllloo'
    """
    doubled = ''
    for char in text:
        doubled += char*2
    return doubled

    # # equivalent using comprehensions
    # return ''.join([char*2 for char in text])


def random_element(a):
    """
    returns random element selected from list a
    """
    return random.choice(a)
    # return a[random.randint(0, len(a)-1)]


def combine_lists_to_dict(keys, values):
    """ returns dict of keys zipped to values

    >>> combine_lists_to_dict(['a', 'b', 'c'], ['apples', 'bananas', 'cherries'])
    {'a': 'apples', 'b': 'bananas', 'c': 'cherries'}
    """
    return dict(zip(keys, values))


def eveneven(nums):
    """ returns if there is an even number of even numbers in num
    :num: list of ints

    >>> eveneven([5, 6, 2])
    True
    >>> eveneven([5, 5, 2])
    False
    """
    evens = [num for num in nums if num % 2 == 0] 
    return len(evens) % 2 == 0

    # evens = []
    # for num in nums:
    #     if num % 2 == 0:
    #         evens.append(num)
    # return len(evens) % 2 == 0


def powers_of_two(n):
    """ returns list of powers of 2 up to the nth power
    :n: int

    >>> powers_of_two(10)
    [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
    """
    return [2**i for i in range(n)]


# scope example
# x = 0
# def looping():
#     x = 10  # local x
#     print('x in func', x)
#     for x in range(10): # local x
#         print('x in loop', x)
#     print('x in func', x)

# looping()
# print('x in main', x)


def missing_char(word):
    """
    returns a list of strings, each missing a different character from word

    >>> missing_char('kitten')
    ['itten', 'ktten', 'kiten', 'kiten', 'kittn', 'kitte']
    """
    # missing = []
    # for i in range(len(word)):
    #     left = word[:i] # 'kitte'
    #     right = word[i+1:] # ''
    #     missing.append(left + right)
    # return missing

    return [word[:i] + word[i+1:] for i in range(len(word))]


def swap_keys_and_values(dictionary):
    """
    returns dictionary with keys and values swapped (using comprehensions)

    >>> swap_keys_and_values({'a': 1, 'b': 2})
    {1: 'a', 2: 'b'}
    """
    return {k: v for (v, k) in dictionary.items()}


def latest_letter(string):
    """ 
    returns letter in string that appears latest in the english alphabet

    >>> latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis')
    'v'
    """
    letters_reversed = sorted(string)
    return letters_reversed[-1]
    
    # another solution
    # return max(string)

    # another solution
    # max_letter = string[0]
    # for letter in string:
    #     if letter > max_letter:
    #         max_letter = letter
    # return max_letter

def common_elements(list1, list2):
    """
    returns list of common elements between list1 and list2 

    >>> common_elements([1,2,3,4], [0,2,4,6])
    [2, 4]
    """
    return [i for i in list1 if i in list2]

    # equivalent to comprehension above
    # common_elem = []
    # for i in list1:
    #     if i in list2:
    #         common_elem.append(i)
    # return common_elem

    # solution using set intersection
    # set1 = set(list1)
    # set2 = set(list2)

    # return list(set1 & set2)


def combine_lists(list1, list2):
    """
    returns combined list of alternating items

    >>> combine_lists([1,2,3], [4,5,6])
    [1, 4, 2, 5, 3, 6]
    """
    # zipped = list(zip(list1, list2))
    # combined = []
    # for i in range(len(zipped)):
    #     combined.append(zipped[i][0])
    #     combined.append(zipped[i][1])
    # return combined

    # combined = []
    # for i in range(len(list1)):
    #     combined.append(list1[i])
    #     combined.append(list2[i])
    # return combined

    return [i for j in zip(list1, list2) for i in j]

    # equivalent to comprehension above
    # combined = []    
    # for j in zip(list1, list2):
    #     print('j', j)
    #     for i in j:
    #         print('i', i)
    #         combined.append(i)
    # return combined


def mean(nums):
    """
    returns avg of nums

    >>> mean([1,1,1,1])
    1.0
    >>> mean([1,2,3,4])
    2.5
    """
    total = 0 
    for num in nums:
        total += num
    return total / len(nums)


def minimum(nums):
    """python python
    returns min of nums

    >>> minimum([1,-1,-9000,999])
    -9000
    >>> minimum([1,2,3,4])
    1
    """
    nums.sort(reverse=True)
    return nums.pop()

    # running_min = float('inf')
    # for num in nums:
    #     if num < running_min:
    #         running_min = num
    # return running_min


def maximum(nums):
    """
    returns max of nums

    >>> maximum([1,-1,-9000,999])
    999
    >>> maximum([1000,2,3,4])
    1000
    """
    # nums.sort()
    # return nums.pop()

    running_max = float('-inf')
    for num in nums:
        if num > running_max:
            running_max = num
    return running_max


def mode(nums):
    """
    returns list of most frequently occuring number(s) in nums

    >>> mode([1,2,3,2])
    [2]
    >>> mode([1,1,1,1])
    [1]
    >>> mode([1,2,3,4])
    [1, 2, 3, 4]
    """
    count = {}
    for num in nums:
        if num not in count:
            count[num] = 1 
        else:
            count[num] += 1

    # return max(count.items(), key=lambda x:x[1])[0]
    modes = []
    max_value = maximum(count.values())
    for k, v in count.items():
        if v == max_value:
            modes.append(k)
    return modes

# print(mode([1,2,4,4]))

from functools import reduce
import time
def combine_all(list_of_lists):
    """
    returns list of all the lists in list_of_lists combined

    >>> combine_all([[5,2,3],[4,5,1],[7,6,3]])
    [5, 2, 3, 4, 5, 1, 7, 6, 3]
    """
    all_nums = []
    # # start = time.clock()
    # for i in range(len(list_of_lists)):
    #     for j in range(len(list_of_lists[i])):
    #         all_nums.append(list_of_lists[i][j])
    # # print(f'nested loop runs in {time.clock() - start}')

    # start = time.clock()
    for i in range(len(list_of_lists)):
        all_nums.extend(list_of_lists[i])
    # print(f'extend loop runs in {time.clock() - start}')

    # # start = time.clock()
    # all_nums = reduce(lambda acc,cur: acc+cur, list_of_lists)
    # # print(f'reduce runs in {time.clock() - start}') 
    return all_nums


def count_letter(letter, word):
    """
    returns the number of letter occurances in word
    
    >>> count_letter('i', 'antidisestablishmenterianism')
    5
    >>> count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis')
    2
    """
    count = 0 
    for char in list(word):
        if char == letter:
            count += 1
    return count


def fibonacci(n):
    """
    returns a list of the first n fibonacci numbers

    >>> fibonacci(10)
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    """
    return [calc_fib(i) for i in range(n)]


def calc_fib(n):
    """
    returns the nth fibonacci number
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return calc_fib(n-2) + calc_fib(n-1)
