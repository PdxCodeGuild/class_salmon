
import os
dir_name = 'csvs'
# cwd = os.getcwd() # using absolute paths
cwd = '.'           # using relative paths
dir_path = os.path.join(cwd, dir_name)
csv_to_dict = {}

# loop through every file in the csvs directory
for file_name in os.listdir(dir_path):
    # only look at csvs
    if file_name.endswith('.csv'): 
        # get file path by joining together the dir path and file name
        file_path = os.path.join(dir_path, file_name)
        with open(file_path) as f:
            # split csvs by newline char
            contents = f.read().split('\n') 

        csv = [] # empty list of dicts
        keys = contents[0] # your keys, aka columns, are the first line in the csv
        keys = keys.split(',') # turn into list
        rows = contents[1:] # your rows are every other line in the csv

        # for each row
        for row in rows:
            row = row.split(',') # turn into list
            row = dict(zip(keys, row)) # turn into dict
            csv.append(row) # add to list 

        # # equivalent way to loop through rows
        # for i in range(1, len(contents)):
        #   row = contents[i]
        #   row = row.split(',') # turn into list
        #   row = dict(zip(keys, row)) # turn into dict
        #   csv.append(row) # add to list 

        csv_to_dict[file_name] = csv # add to dict 

for filename, csv in csv_to_dict.items():
    print(filename)
    for row in csv:
        print(row)