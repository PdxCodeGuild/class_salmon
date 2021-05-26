#name, favorite fruit, favorite color
#merritt, cherry, red
#pete, banana, aquamarine
#john, apple, yellow
#open csv, convert to list of dictionaries
#header is keys
#other lines are values
#e.g. name: merritt, pete, john
#the point is not to use the csv library to make a list of dictionaries
with open('some.csv', 'r') as file:
    lines = file.read().replace('\n', ',').split(',')
    dict_merritt = {}
    dict_merritt[lines[0]] = lines[3]
    dict_merritt[lines[1]] = lines[4]
    dict_merritt[lines[2]] = lines[5]
    dict_pete = {}
    dict_pete[lines[0]] = lines[6]
    dict_pete[lines[1]] = lines[7]
    dict_pete[lines[2]] = lines[8]
    dict_john = {}
    dict_john[lines[0]] = lines[9]
    dict_john[lines[1]] = lines[10]
    dict_john[lines[2]] = lines[11]
    list_of_contacts = [dict_merritt, dict_pete, dict_john]

'''print(list_of_contacts)

    print(dict_merritt, dict_pete, dict_john)
    print(lines)'''
#Version 2
#ask user for each attribute
cols = ['name', 'fruit', 'color']
initiate = input('would you like to begin? yes or no: ')
#if they say yes, collect a bunch of inputs
if initiate == 'yes':
    name1 = input('what is your name?')
    fruit1 = input('what is your favorite fruit?')
    color1 = input('what is your favorite color?')

    name2 = input('What is your friend\'s name?')
    fruit2 = input('What is their favorite fruit?')
    color2 = input('What is your friend\'s favorite color?')

    name3 = input('what is your friend\'s friend\'s name?')
    fruit3 = input('what is your friend\'s friend\'s favorite fruit?')
    color3 = input('what is your friend\'s friend\'s favorite color?')
else:
    ('Cool. See you later.')
#collate the inputs
if initiate == 'yes':
    friend1_dict = {}
    friend1_dict[cols[0]] = name1.lower()
    friend1_dict[cols[1]] = fruit1.lower()
    friend1_dict[cols[2]] = color1.lower()
    friend2_dict = {}
    friend2_dict[cols[0]] = name2.lower()
    friend2_dict[cols[1]] = fruit2.lower()
    friend2_dict[cols[2]] = color2.lower()
    friend3_dict = {}
    friend3_dict[cols[0]] = name3.lower()
    friend3_dict[cols[1]] = fruit3.lower()
    friend3_dict[cols[2]] = color3.lower()
    #print(friend1_dict, friend2_dict, friend3_dict)
#retrieve a record, ask for a name then display their records
name_wanted = input('what is the name you are looking for?').lower()
def check_that_name(name_wanted):
    if friend1_dict['name'] == name_wanted:
        return friend1_dict
    elif friend2_dict['name'] == name_wanted:
        return friend2_dict
    elif friend3_dict['name'] == name_wanted:
        return friend3_dict
    else:
        'bummer, no entry by that name'
print(check_that_name(name_wanted))
#update a record 
#ask the user for a name and the attributes they would like to update
updater_name = input('which name do you want to update attributes for in the log?')
def updater(updater_name, friend1_dict, friend2_dict, friend3_dict):
    if friend1_dict['name'] == updater_name:
        fruit_or_color1 = input(f'which attribute do you want to update in the dictionary for {updater_name}? fruit or color? ')
        if fruit_or_color1 == 'fruit':
            fruit1 = input(f'what is the new favorite fruit for {updater_name}?')
            friend1_dict['fruit'] = fruit1
        if fruit_or_color1 == 'color':
            color1 = input(f'what is the new favorite color for {updater_name}?')
            friend1_dict['color'] = color1
        return friend1_dict
    elif friend2_dict['name'] == updater_name:
        fruit_or_color2 = input(f'which attribute do you want to update in the dictionary for {updater_name}? fruit or color? ')
        if fruit_or_color2 == 'fruit':
            fruit2 = input(f'what is the new favorite fruit for {updater_name}?')
            friend2_dict['fruit'] = fruit2
        if fruit_or_color2 == 'color':
            color2 = input(f'what is the new favorite color for {updater_name}?')
            friend2_dict['color'] = color2
        return friend2_dict
    elif friend3_dict['name'] == updater_name:
        fruit_or_color3 = input(f'which attribute do you want to update in the dictionary for {updater_name}? fruit or color? ')
        if fruit_or_color3 == 'fruit':
            fruit3 = input(f'what is the new favorite fruit for {updater_name}?')
            friend3_dict['fruit'] = fruit3
        if fruit_or_color3 == 'color':
            color3 = input(f'what is the new favorite color for {updater_name}?')
            friend3_dict['color'] = color3
        return friend3_dict
    else:
        'bummer, no entry by that name'
print(updater(updater_name, friend1_dict, friend2_dict, friend3_dict))#cool, that works
#Delete an entry if requested
#I am going to try to repeat the function above with deletions
deleter_name = input('which name do you want to delete from the log?')
def deleter(deleter_name, friend1_dict, friend2_dict, friend3_dict):
    if friend1_dict['name'] == deleter_name:
        del friend1_dict
        return (f'We zapped {deleter_name} from our records.')
    elif friend2_dict['name'] == deleter_name:
        del friend2_dict
        return (f'We zapped {deleter_name} from our records.')
    elif friend3_dict['name'] == deleter_name:
        del friend3_dict
        return (f'We zapped {deleter_name} from our records.')
    else:
        'bummer, no entry by that name'
print(deleter(deleter_name, friend1_dict, friend2_dict, friend3_dict))#this is also working
#Version 3





