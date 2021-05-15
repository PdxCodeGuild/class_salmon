


# for loops can be used with any 'iterable'
# iterable types: range, string, list, dictionary, set
# using for loops with a custom class: https://stackoverflow.com/questions/58658102/how-to-make-a-custom-class-work-with-the-for-in-loop-in-python


# for loops with range


for i in range(10): # for i in range(0, 10, 1)
    print(i, end=' ') # 0 1 2 3 4 5 6 7 8 9
print()

for i in range(5, 10):
    print(i, end=' ') # 5 6 7 8 9
print()

for i in range(10, 21, 2):
    print(i, end=' ') # 10 12 14 16 18 20
print()


for i in range(40, 10, -5):
    print(i, end=' ') # 40 35 30 25 20 15
print()

for i in range(40, 10, 5):
    print(i, end=' ') # does not run even once
print()


# for loops with strings ===========================

text = 'hello world!'
for i in range(len(text)):
    print(i, text[i])
print()

for char in text:
    print(char, end=' ') # h e l l o   w o r l d !
print()


# for loops with lists


nums = [45, 56, 67, 78]
for i in range(len(nums)):
    print(i, nums[i])
print()

for num in nums:
    print(num, end=' ')
print()


# this will alter the element in the list
print(nums)
for i in range(len(nums)):
    nums[i] += 1
print(nums)

# these will not
print(nums)
for num in nums:
    num += 1
print(nums)

print(nums)
for i in range(len(nums)):
    num = nums[i]
    num += 1
print(nums)



# iterate over the indices if you want to use the index to refer to elements in two lists
currencies = ['USD', 'CAD']
countries = ['United States', 'Canada']
output = {}
for i in range(len(currencies)):
    output[countries[i]] = currencies[i]



# for loops with dictionaries

# any immutable type can be used as the key
crazy_dictionary = {
    None: 5,
    6: 6,
    7.0: 'test',
    ('hello', 'world'): 'what?'
}

fruits = {'apples': 1.0, 'bananas': 0.5, 'kiwi': 2.5}
for key in fruits:
    print(key, fruits[key])


for key in fruits.keys():
    print(key, fruits[key])

for value in fruits.values():
    print(value)

for tup in fruits.items():
    print(tup)


