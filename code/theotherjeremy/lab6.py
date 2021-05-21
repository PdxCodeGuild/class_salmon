import random

#____________________Random Card______________________________##
#digits = [(random.randint(1, 9)) for i in range(16)]
# print(digits)

#________________________TEST CARD_________________________________##
#digits = [int(input(f'Enter the first digit of your card:  '))]
# while len(digits) != 16:
#    digits.append(
#        int(input(f'Enter the next digit of your card number:  ')))
# print(digits)

#________________________TEST CARD______________________________##
digits = [4, 5, 5, 6, 7, 3, 7, 5, 8, 6, 8, 9, 9, 8, 5, 5]

check_digit = digits.pop(15)

digits.reverse()


# for i, num in enumerate(digits):
#    if i % 2 == 0:
#        digits[i] = num*2
#    else:
#        num = num

step_4 = [num*2 if i % 2 == 0 else num for i, num in enumerate(digits)]

step_5 = [num - 9 if num > 9 else num for num in step_4]

step_67 = sum(step_5) % 10

print(step_67)
print(check_digit)

print(f'Your card is valid!') if step_67 == check_digit else print(
    'Not a legit card!')
