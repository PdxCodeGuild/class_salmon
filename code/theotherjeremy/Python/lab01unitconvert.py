
user_unit = input(
    'What is your starting unit? \nChoose "ft", "mi", "m", "km", "yard", or "inch"\n  ')
user_dist = input('What is the distance?  ')
conv_unit = input(
    'What is the final unit? \nChoose "ft", "mi", "m", "km", "yard", or "inch"\n  ')
conv_dict = {'m': 1,
             'ft': .3048,
             'mi': 1609.34,
             'km': 1000,
             'inch': .0254,
             'yard': .9144}

if user_unit in conv_dict.keys():
    meters = float(user_dist) * (conv_dict[user_unit])


fin_dict = {'m': 1,
            'ft': 1/.3048,
            'mi': 1/1609.34,
            'km': 1/1000,
            'inch': 1/.0254,
            'yard': 1/.9144}

result = meters * (fin_dict[conv_unit])

print(f'{user_dist} {user_unit} is {result} {conv_unit}')
print('The metric system is superior!!')
