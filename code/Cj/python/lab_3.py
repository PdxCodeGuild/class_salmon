num = int(input('Enter a number from 1 to 999: '))
while num > 999:
    print('User Error: Number too large! ')
    num = int(input('Enter a number from 1 to 999: '))
hundreds_digit = num//100
x = num//10
tens_digit = x%10
ones_digit = num%10

tens_table = {
2: 'Twenty',
3: 'Thirty',
4: 'Fourty',
5: 'Fifty',
6: 'Sixty',
7: 'Seventy',
8: 'Eighty',
9: 'Nintey',
}
ones_table = {
    0: '',
    1: 'One',
    2: 'Two',
    3: 'Three',
    4: 'Four',
    5: 'Five',
    6: 'Six',
    7: 'Seven',
    8: 'Eight',
    9: 'Nine',
    10: 'Ten',
    11: 'Eleven',
    12: 'Twelve',
    13: 'Thirteen',
    14: 'Fourteen',
    15: 'Fifteen',
    16: 'Sixteen',
    17: 'Seventeen',
    18: 'Eighteen',
    19: 'Ninteen',
}



if num > 99:
    teens = num % 100
    if teens < 20:
        output = f'{ones_table[hundreds_digit]} Hundred {ones_table[teens]} '
    elif tens_digit < 2:
        output = ones_table[num]
    # elif ones_digit == 0:
    #     output = tens_table[tens_digit] 
    else:
        output = f'{ones_table[hundreds_digit]} Hundred {tens_table[tens_digit]} {ones_table[ones_digit]} '
else:   
    if tens_digit < 2:
        output = ones_table[num]
    elif ones_digit == 0:
        output = tens_table[tens_digit] 
    else:
        output = f'{tens_table[tens_digit]}-{ones_table[ones_digit]} '
    
    
print(output)