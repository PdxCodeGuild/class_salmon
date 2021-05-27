#name, favorite fruit, favorite color
#merritt, cherry, red
#pete, banana, aquamarine
#john, apple, yellow
#open csv, convert to list of dictionaries
#header is keys
#other lines are values
#e.g. name: merritt, pete, john
#the point is not to use the csv library to make a list of dictionaries
#Reattempt of Version 1 Lab 10 contact lists

with open('some.csv', 'r') as file:
    file.readline()#gets rid of headers
    lines = file.read()    
    #print(lines) #I am not sure if lines and list_of_lines are any different. They appear to be printing the same way. 
    list_of_lines = lines.replace('\n', ',').split(',')#now the pattern is the same - name, fruit, color
    print(list_of_lines)
    len_list_lines = len(list_of_lines)
    print(len_list_lines)
fillable_list = []
def make_a_dict(list_of_lines, len_list_lines, fillable_list):
    #cols = ['name', 'fruit', 'color'] #used this in the key: value, value, value version
    #dict_csv = {} #used this in the key: value, value, value version
    #fillable_list = []
    counter = 0
    while counter < len_list_lines:
        new_entry = {'name': list_of_lines[0], 'fruit': list_of_lines[1], 'color': list_of_lines[2]}
        list_of_lines.pop(0)#pop three list items off in sequence
        list_of_lines.pop(0)
        list_of_lines.pop(0)
        fillable_list.append(new_entry)
        '''for n in cols: #this is the key: value, value, value version
            if counter <= 2:
                dict_csv[n] = [list_of_lines[counter]]
            else:
                dict_csv[n].append(list_of_lines[counter])
            #remove the first item in list
            #list_of_lines.pop(0)'''
        counter +=3 #since all the items in the list are in order, delimited by a commma, then name, fruit, color = 3
    else:
        return fillable_list
print(make_a_dict(list_of_lines, len_list_lines, fillable_list))
print(fillable_list)
#Reattempt of Version 2

#Create function
#Version 2
#ask user for each attribute
def create(fillable_list):
    create_dict = {}
    initiate = input('would you like to begin creating a new entry? yes or no: ')
    #if they say yes, collect a bunch of inputs
    if initiate == 'yes':
        create_dict['name'] = 'nick' #input('what is the new name? ')
        create_dict['fruit'] = 'orange' #input('what is their favorite fruit? ')
        create_dict['color'] = 'blue' #input('what is their favorite color? ')
        fillable_list.append(create_dict)
        #how can I get this to go back to initiate?
        return fillable_list
    else:
        print('Cool. See you later.')
        return #need to stop the loop here
#print(create(fillable_list))#this is working
#retrieve a record, ask for a name then display their records

def retrieve():
    name_wanted = input('what is the name you are looking for?').lower()
    for key, value in enumerate(fillable_list):#must include the value spot in this enumerate thing, because of how it reads the list of dicts
        if fillable_list[key]['name'] == name_wanted: #this was working, then it stopped - you must put for key, value in enumerate, you cannot leave out the value place
            return fillable_list[key]
        if fillable_list[key]['name'] != name_wanted:
            break
        '''else:
            print('bummer, no entry by that name')'''#this else statement is returning for every item in the list of dicts
#print(retrieve())#this finally works
#update a record, attempt 75
#ask the user for a name and the attributes they would like to update

def updater():
    updater_name = 'merritt' #input('which name do you want to update attributes for in the log?').lower()
    for key, value in enumerate(fillable_list):#must include the value spot in this enumerate thing, because of how it reads the list of dicts
        if fillable_list[key]['name'] == updater_name: #this was working, then it stopped - you must put for key, value in enumerate, you cannot leave out the value place
                fruit_or_color = 'fruit' #input(f'which attribute do you want to update in the dictionary for {updater_name}? fruit or color? ').lower()
                if fruit_or_color == 'fruit':
                    fruit = 'orange' #input(f'what is the new favorite fruit for {updater_name}?')
                    fillable_list[key]['fruit'] = fruit
                    return fillable_list[key]
                if fruit_or_color == 'color':
                    color = 'pink' #input(f'what is the new favorite color for {updater_name}?')
                    fillable_list[key]['color'] = color
                    return fillable_list[key]
        else:
            return ('bummer, no entry by that name')
#print(updater())#cool, that works
#Delete an entry if requested

def deleter():
    deleter_name = 'merritt' #input('which name do you want to delete from the log?').lower()
    for key, value in enumerate(fillable_list):#must include the value spot in this enumerate thing, because of how it reads the list of dicts
        if fillable_list[key]['name'] == deleter_name:
            del fillable_list[key]
            return (f'We zapped {deleter_name} from our records.')
        else:
            'bummer, no entry by that name'
#print(deleter())#this is also working
#print(fillable_list) #check that the program actually deleted the entry
#make all of this accessible through another function
def decide_to_do_something():
    decision = input('what do you want to do - (c)reate an entry, (d)elete an entry, (r)etrieve an entry, or (u)pdate an entry, or (done) doing stuff? ')
    while decision != 'done':
        if decision == 'c':
            print(create(fillable_list))
        elif decision == 'd':
            print(deleter())
        elif decision == 'r':
            print(retrieve())
        elif decision == 'u':
            print(updater())#this is where while loop ends
        decision = input('what do you want to do - (c)reate an entry, (d)elete an entry, (r)etrieve an entry, or (u)pdate an entry, or (done) doing stuff? ').lower()
    if decision == 'done':
        return('thanks for stopping by')

print(decide_to_do_something())
#Version 3
#write the updated contact info to a CSV
print(fillable_list)
#make a list
cols = ['name', 'fruit', 'color']

#try list comprehension where the column headers I deleted earlier will serve as keys 
list_of_lists = [[row[key] for key in cols] for row in fillable_list]
#just_a_list = [row[key] for key in cols for row in fillable_list] #this is just a list. I could put this through a function to sort. That would be more work.
#this looks like [['merritt', 'cherry', 'red'], ['pete', 'banana', 'aquamarine'], ['john', 'apple', 'yellow']]
#now need to append with cols
list_of_lists.insert(0, cols)#0 is the positional, the second arg is what goes into list.
print(list_of_lists)#now looks like [['name', 'fruit', 'color'], ['merritt', 'cherry', 'red'], ['pete', 'banana', 'aquamarine'], ['john', 'apple', 'yellow']]

with open('some_output_lab10.csv', 'w') as output_list_file: 
        for name, fruit, color in list_of_lists:
            list_entry = f'{name}, {fruit}, {color}\n'
            output_list_file.write(list_entry)
#below this line is a bunch of useless junk           
'''#reading 
with open('some_output_lab10.csv') as output_list_file:
    output_data = output_list_file.read().split('\n')
#with open('some_output_lab10.csv', 'r') as output_list_file:
    lines2 = output_list_file.read()    
    #print(lines) #I am not sure if lines and list_of_lines are any different. They appear to be printing the same way. 
    list_of_lines2 = lines2.replace('\n', ',').split(',')#now the pattern is the same - name, fruit, color
    print(list_of_lines2)
    len_list_lines2 = len(list_of_lines2)
    #print(len_list_lines2)
phone_book = {}
for line in phone_book_data:
    name, number = line.split()
    phone_book[name] = number'''
#to start, we take the previous outputs of Version 2 then send it to a csv
#test to get a regular csv working'''
'''phonebook = {'David': '5551234', 'Alice': '6662345'}
#write the stuff
with open('phonebook.csv', 'w') as phone_book_file:
    for name, number in phonebook.items():
        line = f'{name} {number}\n'
        phone_book_file.write(line)
print(phone_book_file)
#read the stuff
with open('phonebook.csv') as phone_book_file:
    phone_book_data = phone_book_file.read().split('\n')
#print the stuff
print(phone_book_data)'''#cool. I think i understand how this works.

#with open('output_lab10.csv', 'w') as output_list_file:
    #since the user may or may not have deleted stuff, check with try statements to see if dict still exists.
    #this seems easier than packing, unpacking, then repacking a list of dictionaries.
'''try:
    friend1_dict
except NameError:
    friend1_dict = None
    if friend1_dict != None:
        #this .items() is not working
        for name, fruit, color in friend1_dict.items():
            line = f'{name}{fruit}{color}\n'
            with open('output_lab10.csv', 'w') as output_list_file:
                output_list_file.write(line)
try:
    friend2_dict
except NameError:
    friend2_dict = None
    if friend2_dict != None:
        for name, fruit, color in friend2_dict.items():
            line = f'{name}{fruit}{color}\n'
            with open('output_lab10.csv', 'w') as output_list_file:
                output_list_file.write(line)
try:
    friend3_dict
except NameError:
    friend3_dict = None
    if friend3_dict != None:
        for name, fruit, color in friend3_dict.items():
            line = f'{name}{fruit}{color}\n'
            with open('output_lab10.csv', 'w') as output_list_file:
                output_list_file.write(line)
finally:
    'There is no there, there.'#not sure if this edge case would work
print(output_list_file)#this is not working in the GUI
#now check to see if that worked by reading it.'''
'''with open('output_lab10.csv') as ouput_list_file:
    output_list_data = output_list_file.read().split('\n')
#print the stuff
print(output_list_data)'''

