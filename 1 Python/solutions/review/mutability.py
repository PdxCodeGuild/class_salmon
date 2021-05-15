

# immutable types: int, float, string, tuples
# mutable types: list, dictionary, set


# side effects - a side effect of a function is when a function changes some data unexpectly

def sort(nums):
    nums.sort()
    nums.append(67)
    return nums

nums = [23, 78, 56, 34]
nums2 = sort(nums)
print(nums)

import random
random.shuffle(nums)
print(nums)

def exclaim(text):
    text += '!!!!'
    return text

text = 'hello'
exclaimed_hello = exclaim(text)
print(text)


# methods/operators on immutable types return copies
# methods/operators on mutable types edit the original

text = 'hello'
# text.upper() # bad
text = text.upper()
print(text)

nums = [23, 78, 56, 34]
# nums = nums.sort() # bad
nums.sort()
print(nums)

