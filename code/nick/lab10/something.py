'''#Reattempt of Version 1 Lab 10 contact lists

with open('some.csv', 'r') as file:
    file.readline()#gets rid of headers
    lines = file.read()    
    #print(lines) #I am not sure if lines and list_of_lines are any different. They appear to be printing the same way. 
    list_of_lines = lines.replace('\n', ',').split(',')#now the pattern is the same - name, fruit, color
    print(list_of_lines)
    len_list_lines = len(list_of_lines)
    print(len_list_lines)
def make_a_dict(list_of_lines, len_list_lines):
    #cols = ['name', 'fruit', 'color'] #used this in the key: value, value, value version
    #dict_csv = {} #used this in the key: value, value, value version
    empty_list = []
    counter = 0
    while counter < len_list_lines:
        new_entry = {'name': list_of_lines[0], 'fruit': list_of_lines[1], 'color': list_of_lines[2]}
        list_of_lines.pop(0)#pop three list items off in sequence
        list_of_lines.pop(0)
        list_of_lines.pop(0)
        empty_list.append(new_entry)
        for n in cols: #this is the key: value, value, value version
            if counter <= 2:
                dict_csv[n] = [list_of_lines[counter]]
            else:
                dict_csv[n].append(list_of_lines[counter])
            #remove the first item in list
            #list_of_lines.pop(0)
        counter +=3 #since all the items in the list are in order, delimited by a commma, then name, fruit, color = 3
    else:
        return empty_list
print(make_a_dict(list_of_lines, len_list_lines))

        #list_of_lines[1] = dict(cols[1])'''
'''answer = {}
with open('some.csv', 'r') as file: 
    for line in infile:
        year, gender, name, count = (s.strip('"') for s in line.split(','))
        key = (name, gender)
        if key not in answer: answer[key] = {}
        answer[key][int(year)] = (int(count), None)'''
#for list_of_lines[0]
#print each step. make a dictionary with key:value pair unique variable for headers first line.
'''fillable_list = [{'name': 'nick', 'fruit': 'orange'}]  
def retrieve():
    name_wanted = input('what is the name you are looking for?').lower()
    for key in enumerate(fillable_list):
        if fillable_list[key]['name'] == name_wanted: #this was working, then it stopped
            return fillable_list[key]
    else:
        ('bummer, no entry by that name')
print(retrieve())'''

#below is a code snippet I took from John about collating the list of dictionaries into a list without list comprehension
list_of_dictionaries = [{'name': 'Sarah', 'favorite animal': 'dog', 'favorite color': 'blue'}, {'name': 'Taylor', 'favorite animal': 'giraffe', 'favorite color': 'green'}, {'name': 'Taylor', 'favorite animal': 'giraffe', 'favorite color': 'green'}, {'name': 'Kyle', 'favorite animal': 'monkey', 'favorite color': 'red'}]
string_to_output = ''
for x in range(len(list_of_dictionaries)):
    if x == 0:
        headers = list(list_of_dictionaries[x].keys())#this takes the keys and puts them in a list
        print(headers)
        headers_string = ','.join(headers)#.join()combines the elements of a list into a single string, separated by a delimiter
        print(headers_string)
        string_to_output += headers_string + '\n'#this puts headers in the first positions for the whole .csv
        print(string_to_output)
    list_new = list(list_of_dictionaries[x].values())
    #print(list_new)
    string_new = ','.join(list_new) 
    #print(string_new)
    string_to_output += string_new + '\n'

#print(string_to_output)
