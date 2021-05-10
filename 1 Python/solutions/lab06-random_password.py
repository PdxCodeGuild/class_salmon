"""
Lab 6: generate a random password
"""

import random

characters = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJK@$%#^'
n = int(input('Enter your desired password length: '))
password = ''

for i in range(n):
    password += random.choice(characters)
print(password)

# # alternatively, use a while loop instead of a for-loop 
# i = 0
# while i < n:
#     password += random.choice(characters)
#     i += 1 		# i = i + 1
# print(password)
