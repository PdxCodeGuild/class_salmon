num_list =[]
trigger = True
while trigger is True:
    UI = input('Enter a Number or type "done" to finish: ')
    if UI.isnumeric():
        num_list.append(UI)
    while not UI.isnumeric():
        if UI == 'done':
            trigger = False
            break
        else:
            print('Sorry, can\'t do math without numbers bud. Try entering a number. ')
            break
total = 0
for item in num_list:
    total += int(item)
average = total / len(num_list)
print(f'The total is {total} and the average of the listed numbers provided was {average}. ')
# print(num_list)