

import random
nums = [random.randint(0, 99) for i in range(100)]
print(nums)




names = ['David', 'Helen', 'Anne']
# getting lowercase names that don't start with 'A'
lower_names = [name.lower() for name in names if name[0] != 'A']
print(lower_names)




