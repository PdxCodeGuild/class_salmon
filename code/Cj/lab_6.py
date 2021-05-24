def validate(card_number):
    card_number = list(card_number)
    card_number = [int(index) for index in card_number]   
    check_digit = card_number.pop(-1)
    card_number.reverse()
    card_number = [card_number[index] * 2 if index % 2 == 0 else card_number[index] for index in range(len(card_number))]
    card_number = [card_number[index] - 9 if card_number[index] > 9 else card_number[index] for index in range(len(card_number))]
    total = sum(card_number)
    if total % 10 == check_digit:
        return True
    else:
        return False
     
card_number = input('Enter Credit Card Number: ')
output = 'Card Number Valid!' if validate(card_number) is True else 'Invalid Card Number! '
print(output)
# card_number = input('Enter Credit Card Number: ')
# if validate(card_number) is True:
#     print('Card Number Valid!')
# else:
#     print('Invalid Card Number! ')



