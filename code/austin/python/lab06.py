def check_card():
    card_num = input('Please input your card number with no spaces! ')
    num_list = [int(num) for num in card_num]
    last_num = num_list.pop()
    num_list.reverse()
    for i,num in enumerate(num_list):
        if i % 2 != 1:
            num_list[i] *= 2
    for i,num in enumerate(num_list):
        if num > 9:
            num_list[i] -=9
    if (int(str(sum(num_list))[-1])) == last_num:
        return True
    else:
        return False
    return num_list
def is_valid():
    if check_card() == True:
        return 'Valid'
    else:
        return 'Invalid'