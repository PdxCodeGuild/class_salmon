user_input = int(input('Enter a number between 0 and 999: '))

hundreds = user_input//100
teens = user_input%100
tens = (user_input%100)//10
ones = user_input%10

ones_dict = { 1: 'one',
2: 'two',
3: 'three',
4: 'four',
5: 'five',
6: 'six',
7: 'seven',
8: 'eight',
9: 'nine',
10: 'ten',
11: 'eleven',
12: 'twelve',
13: 'thirteen',
14: 'fourteen',
15: 'fifteen',
16: 'sixteen',
17: 'seventeen',
18: 'eighteen',
19: 'nineteen',
}

tens_dict = { 2: 'twenty',
3: 'thirty',
4: 'fourty',
5: 'fifty',
6: 'sixty',
7: 'seventy',
8: 'eighty',
9: 'ninety',
}

hundreds_dict = { 1: 'one-hundered',
2: 'two-hundred',
3: 'three-hundered',
4: 'four-hundred',
5: 'five-hundred',
6: 'six-hundred',
7: 'seven-hundred',
8: 'eight-hundred',
9: 'nine-hundred',
}

if tens == 0 and ones == 0:
    result = f'{hundreds_dict[hundreds]}'

elif hundreds > 0 and teens < 20:
    result = f'{hundreds_dict[hundreds]} - {ones_dict[teens]}'   

elif tens < 2 and hundreds == 0:
    result = ones_dict[user_input]

elif hundreds == 0: 
    if ones == 0:
        result = f'{tens_dict[tens]}'
    else:
        result = f'{tens_dict[tens]}-{ones_dict[ones]}'

elif hundreds > 0:
    result = f'{hundreds_dict[hundreds]}-{tens_dict[tens]}-{ones_dict[ones]}'
 
print(result)