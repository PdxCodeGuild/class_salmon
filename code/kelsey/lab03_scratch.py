# Lab 3: Number to Phrase

user_number = input('Enter a number 0-999: ')

hundreds_digit = int(user_number) % 100
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

def number_to_phrase(number):
    if int(number) == 0:
        return f'zero'
    elif int(number) < 10:
        return ones_digit_dict[number]
    elif hundreds_digit == 0:
        return f'{ones_digit_dict[number[0]]}-hundred' 
    else:
        return f'{tens_digit_dict[number[0]]}- {ones_digit_dict[number[1]]}'
    

print(number_to_phrase(user_number))