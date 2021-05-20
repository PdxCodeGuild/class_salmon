# Lab 3: Number to Phrase
# Convert a given number into its English representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.
number = input('Enter a number 0-99: ')

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

if int(number) == 0:
    print('zero')
elif int(number) < 20:
    print(ones_digit_dict[number])
else:
    if int(number[1]) == 0:
        print(tens_digit_dict[number[0]])
    else:
        print(tens_digit_dict[number[0]] + '-' + ones_digit_dict[number[1]])


# Version 2
# Handle numbers from 100-999.

big_num = input('Enter a number 100-999: ')

def number_to_phrase(number):
    hundreds_digit = f'{ones_digit_dict[number[0]]}-hundred'
    tens_digit = f' and {tens_digit_dict[number[1]]}'
    ones_digit = f'-{ones_digit_dict[number[2]]}'

    number_as_phrase = hundreds_digit + tens_digit + ones_digit
    return number_as_phrase

print(number_to_phrase(big_num))