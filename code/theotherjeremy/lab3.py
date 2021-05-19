x = int(input('Gimme a number from 0 - 99:  '))
tens = x//10
ones = x % 10

ones_dict = {0: 'zero',
             1: 'one',
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

tens_dict = {2: 'twenty',
             3: 'thirty',
             4: 'forty',
             5: 'fifty',
             6: 'sixty',
             7: 'seventy',
             8: 'eighty',
             9: 'ninety'}


if tens < 2:  # or ones == 0:
    print(ones_dict[x])

else:
    if ones == 0:
        print(tens_dict[tens])
    else:
        print(f'{tens_dict[tens]}{ones_dict[ones]}')

# elif tens < 2 or ones == 0:
#    ones in ones_dict:
#    print(ones_dict[ones])
# print(tens)
# print(ones)
