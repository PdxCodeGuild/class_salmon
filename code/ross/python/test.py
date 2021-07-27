""""fruits = ["apples", "bananas", "cerry"]
print(fruits)

# upper_fruits = [fruit.upper() for fruit in fruits]
print(fruit.upper(fruit)) for fruit in fruits"""

'''
nums = [1, 2, 3, 4]

new_nums = [(num**2)*2 for num in nums]

print(new_nums)
'''



'''people = ['bob', 'joe', 'jane', 'bob']

bobs_only = [person for person in people if person.startswith('bob')]
print(bobs_only)'''



'''nums = range(20)
print(nums)
double_even_nums = [(num*2 if num % 2 == 0 else num) for num in nums]

print(double_even_nums)'''

'''list1 = [3, 4, 5, 4, 5, 6,]
list2 = [1, 2, 2, 4, 5, 6,]

matches = [match + 1 for match in list1 if list1[match - 1] == list2[match - 1]]
print(matches)'''
'''
fruits  = ["aookes", 'bananas', ' cherries']

for i, fruit in enumerate(fruits):
    print(list(enumerate(fruits)))'''

tuples = ('husky', 'doggo', 'chile') # use parantheses instead of square brackets like lists. Tuples are immutable
print(tuples)