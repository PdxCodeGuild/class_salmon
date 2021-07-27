from random import randint
def pic_6():
    numbers=[randint(1,99) for num in range(6)]
    return(numbers)
def num_matches():
    winning_nums=pic_6()
    entry_nums=pic_6()
    matches=0
    for i in range(6):
        if winning_nums[i] == entry_nums[i]:
            matches+=1
    return matches
def play_100000():
    money = 0
    plays = 100000
    while plays > 0:
        money -= 2
        plays -= 1
        matches = num_matches()
        if matches == 0:
            money+=0
            continue
        elif matches == 1:
            money += 4
            continue
        elif matches == 2:
            money += 7
            continue
        elif matches == 3:
            money += 100
            continue
        elif matches == 4:
            money += 50000
            continue
        elif matches == 5:
            money += 1000000
            continue
        elif matches == 6:
            money += 25000000
            continue
    roi = money / 200000
    return f'Final balcance: ${money}\nROI: {roi}\nExpenses: $200000\nEarnings: ${money + 200000}'