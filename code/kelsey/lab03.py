# Lab 3: Number to Phrase
# Convert a given number into its English representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.
number = input('Enter a number 0-99: ')

def split(number):
    return [num for num in number]

number = split(number) # [*'tens_digit', 'ones_digit']

def number_to_phrase(ones_digit, tens_digit=0):
    tens_digit = number // 10
    ones_digit = number % 10
    number_as_word = tens_digit + ones_digit
    return 

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
    '9': 'nine'
}

tens_digit_dict = {
    '0': '',
    '10': 'teen',
    '2': 'twenty',
    '3': 'thirty',
    '4': 'forty',
    '5': 'fifty',
    '6': 'sixty',
    '7': 'seventy',
    '8': 'eighty',
    '9': 'ninety'
}


# x = 67
# tens_digit = x//10
# ones_digit = x%10

# Hint 2: use the digit as an index for a list of strings OR as a key for a dict of digit:phrase pairs.

# Version 2
# Handle numbers from 100-999.

# Version 3 (optional)
# Convert a number to roman numerals.

# Version 4 (optional)
# Convert a time given in hours and minutes to a phrase.