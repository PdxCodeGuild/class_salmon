def convert_string(y): # loop string, convert item in string into an integer
    converted_list = []
    for i, value in enumerate(credit_card):
       converted_list.append(int(value))
    return converted_list

def double_evens(x):
    converted_list = []
    for i, value in enumerate(x):
        if i % 2 == 0:
            y = value * 2
            converted_list.append(y)
        else: 
            y = value
            converted_list.append(y)
    return converted_list
        

credit_card = '4556737586899858'
credit_card = list(credit_card)
credit_card = convert_string(credit_card)

check_digit = credit_card.pop(-1)
credit_card.reverse()    
credit_card = double_evens(credit_card)

credit_card = [num - 9 if num > 9 else num for num in credit_card]

total = sum(credit_card)

output = 'Card Validated! ' if total % 10 == check_digit else 'Card not Valid '
print(output)