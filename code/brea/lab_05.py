import random

balance = 0
winning_numbers = []
matches = 0
winning_value = 0
user_numbers = []
y = ''
confirm = False

def win_checker(*parameters):
    for parameter in parameters: 
        if parameter in winning_numbers:
            matches += 1
    return matches

def winning_ticket():
    for x in range(6):
    x = (random.randint(0,99))
    winning_numbers.append(x)
    print(winning_numbers)

def 
    for x in range(10):
    balance += (-2)

for x in range(6):
    y = int(input('Enter your ticket numbers: '))
    while y > 99:
        y = input('Please make a valid entry: ')
    user_numbers.append(y)
print(user_numbers)



# print(output)