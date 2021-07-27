# Lab 3: Number to Phrase
# Convert a given number into its English representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.
# Version 2
# Handle numbers 100-999.

user_number = input('Enter a number 0-999: ')

hundreds_digit = int(user_number) // 100
tens_digit = int(user_number) // 10
ones_digit = int(user_number) % 10

ones_digit_dict = {
    '0': '',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
}

tweens_dict = {
    '10': 'ten',
    '11': 'eleven',
    '12': 'twelve',
    '13': 'thirteen',
    '14': 'fourteen',
    '15': 'fifteen',
    '16': 'sixteen',
    '17': 'seventeen',
    '18': 'eighteen',
    '19': 'nineteen'
}

tens_digit_dict = {
    '0': '',
    '2': 'twenty',
    '3': 'thirty',
    '4': 'forty',
    '5': 'fifty',
    '6': 'sixty',
    '7': 'seventy',
    '8': 'eighty',
    '9': 'ninety'
}

if int(user_number) == 0: # 0 only
    print('zero')
elif 0 < int(user_number) < 10: # 1-9
    print(f'{ones_digit_dict[user_number]}')
elif 10 <= int(user_number) < 20: # 10-19
    print(f'{tweens_dict[user_number]}')
elif hundreds_digit == 0 and ones_digit == 0: # straight tens (10, 20, 30, etc.)
    print(f'{tens_digit_dict[user_number[0]]}')
elif 21 <= int(user_number) <= 99: # any two-digit number greater than 20, where both digits are not 0
    print(f'{tens_digit_dict[user_number[0]]}-{ones_digit_dict[user_number[1]]}')
elif hundreds_digit != 0 and int(user_number[1]) == 0 and ones_digit == 0:
    print(f'{ones_digit_dict[user_number[0]]}-hundred') # straight hundreds (100, 200, 300, etc.)
elif hundreds_digit != 0 and int(user_number[1]) == 0 and ones_digit != 0: # hundreds + only 1-9
    print(f'{ones_digit_dict[user_number[0]]}-hundred and {ones_digit_dict[user_number[2]]}')
elif hundreds_digit != 0 and int(user_number[1]) == 1: # hundreds + only 10-19
    tween = int(user_number) - int(user_number[0])*100
    tween = str(tween)
    print(f'{ones_digit_dict[user_number[0]]}-hundred and {tweens_dict[tween]}')
elif int(user_number[1]) != 0 and ones_digit == 0: # straight hundreds + straight tens// all ones digits are zero
    print(f'{ones_digit_dict[user_number[0]]}-hundred and {tens_digit_dict[user_number[1]]}')
else: # remaining three-digit numbers, where all three digits are not zero
    print(f'{ones_digit_dict[user_number[0]]}-hundred and {tens_digit_dict[user_number[1]]}-{ones_digit_dict[user_number[2]]}')