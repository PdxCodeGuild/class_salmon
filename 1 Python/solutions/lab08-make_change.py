"""
Lab 8: break an amount into quarters, dimes, nickles, pennies
"""

# version 1: the user will enter something like 136, representing $1.36
# amount = input('enter the total amount, in pennies: ')

# version 2: the user will enter something like 1.36
money = round(float(input('Enter amount you want to break change: $')) * 100)

dollars = money // 100
money %= 100
quarters = money // 25
money %= 25
dimes = money // 10 
money %= 10 
nickles = money // 5
money %= 5
pennies = money

print(f'Your change is {dollars} dollar(s), {quarters} quarter(s), {dimes} dime(s), {nickles} nickle(s), {pennies} penny(ies).')