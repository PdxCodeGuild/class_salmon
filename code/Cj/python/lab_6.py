def validate(cc_num):
    cc_num = list(cc_num)
    cc_num = [int(index) for index in cc_num]   
    check_digit = cc_num.pop(-1)
    cc_num.reverse()
    cc_num = [cc_num[index] * 2 if index % 2 == 0 else cc_num[index] for index in range(len(cc_num))]
    cc_num = [cc_num[index] - 9 if cc_num[index] > 9 else cc_num[index] for index in range(len(cc_num))]
    total = sum(cc_num)
    if total % 10 == check_digit:
        return True
    else:
        return False
     
cc_num = input('Enter Credit Card Number: ')
output = 'Card Number Valid!' if validate(cc_num) is True else 'Invalid Card Number! '
print(output)
# card_number = input('Enter Credit Card Number: ')
# if validate(card_number) is True:
#     print('Card Number Valid!')
# else:
#     print('Invalid Card Number! ')



