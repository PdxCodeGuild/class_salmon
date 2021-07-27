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
    counter = 0
    while counter < len_list_lines:
        new_entry = {'name': list_of_lines[0], 'fruit': list_of_lines[1], 'color': list_of_lines[2]}
        list_of_lines.pop(0)#pop three list items off in sequence
        list_of_lines.pop(0)
        list_of_lines.pop(0)
        fillable_list.append(new_entry)
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
        create_dict['name'] = input('what is the new name? ')
        create_dict['fruit'] = input('what is their favorite fruit? ')
        create_dict['color'] = input('what is their favorite color? ')
        fillable_list.append(create_dict)
        #how can I get this to go back to initiate?
        return fillable_list
    else:
        print('Cool. See you later.')
        return #need to stop the loop here
#print(create(fillable_list))#this is working
#retrieve a record, ask for a name then display their records

def retrieve():
    fetched_name = []
    name_wanted = input('what is the name you are looking for? ').lower()
    for key in fillable_list:#must include the value spot in this enumerate thing, because of how it reads the list of dicts
        if key['name'] == name_wanted: #this was working, then it stopped - you must put for key, value in enumerate, you cannot leave out the value place
            fetched_name.append(key)
            return fetched_name
            
#ask the user for a name and the attributes they would like to update

def updater():
    updater_name = input('which name do you want to update attributes for in the log? ').lower()
    for number, key in enumerate(fillable_list):#must include the value spot in this enumerate thing, because of how it reads the list of dicts
        if key['name'] == updater_name:
            fruit_or_color = input(f'which attribute do you want to update in the dictionary for {updater_name}? fruit or color? ').lower()
            if fruit_or_color == 'fruit':
                fruit = input(f'what is the new favorite fruit for {updater_name}? ')
                key['fruit'] = fruit
                return fillable_list[number]
            if fruit_or_color == 'color':
                color = input(f'what is the new favorite color for {updater_name}? ')
                key['color'] = color
                return fillable_list[number]

#Delete an entry if requested

def deleter():
    deleter_name = input('which name do you want to delete from the log?').lower()
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
# print(fillable_list)
#make a list
cols = ['name', 'fruit', 'color']

#try list comprehension where the column headers I deleted earlier will serve as keys 
list_of_lists = [[row[key] for key in cols] for row in fillable_list]
# print(list_of_lists)
#just_a_list = [row[key] for key in cols for row in fillable_list] #this is just a list. I could put this through a function to sort. That would be more work.
#this looks like [['merritt', 'cherry', 'red'], ['pete', 'banana', 'aquamarine'], ['john', 'apple', 'yellow']]
#now need to append with cols
list_of_lists.insert(0, cols)#0 is the positional, the second arg is what goes into list.
# print(list_of_lists)#now looks like [['name', 'fruit', 'color'], ['merritt', 'cherry', 'red'], ['pete', 'banana', 'aquamarine'], ['john', 'apple', 'yellow']]

with open('some_output_lab10.csv', 'w') as output_list_file: 
        for name, fruit, color in list_of_lists:
            list_entry = f'{name}, {fruit}, {color}\n'
            output_list_file.write(list_entry)
#below this line is a bunch of useless junk           
