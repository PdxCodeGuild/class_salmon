x = int(input('Gimme a number from 0 - 99:  '))

hunds = x//100

tens = (x % 100) // 10

ones = x % 10
if x > 1 and ones == 0:
    ones = ''

ones_dict = {'': '',
             0: 'zero',
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

tens_dict = {0: '',
             2: 'twenty',
             3: 'thirty',
             4: 'forty',
             5: 'fifty',
             6: 'sixty',
             7: 'seventy',
             8: 'eighty',
             9: 'ninety'}


if tens < 2 and x < 20:
    print(ones_dict[x])

else:
    if ones == 0 and x < 100:
        print(tens_dict[tens])
    else:
        if x < 99:
            print(f'{tens_dict[tens]} {ones_dict[ones]}')
        else:
            print(
                f'{ones_dict[hunds]} hundred {tens_dict[tens]} {ones_dict[ones]}')
