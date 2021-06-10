"""

Author: Jeremy Bush
Project: Radio Utilities in Python (RUPy), Winlink Express Utility Library
Version: 1
Date: 6/9/2021

"""


import os  # needed to build path
import requests
import shutil
import csv


# Update Winlink config file with new grid square
# Hard coded for now.  Need to convert this to a dynamic file path at some point.
def update_winlink_config(grid_square):
    filepath = os.path.join('C:\\', 'RMS Express', 'RMS Express.ini')
    # Create backup of config file prior to modifying
    shutil.copyfile(filepath, filepath+'.backup')
    # Read file for editing
    with open(filepath, 'r') as file:
        lines = file.read().split('\n')
    # Convert each list into a list of its own
    lines = [line.split(',') for line in lines]
    index = 0
    search_text = 'Grid Square'
    for line in range(len(lines)):
        if search_text in lines[line]:
            lines[line] = 'Grid Square=' + grid_square
            break
    with open(filepath, 'w') as file:
        for line in lines:
            if lines.index(line) != len(lines) - 1:
                file.write(line + '\n')
            else:
                file.write(line)


# download updated winlink node list
def update_winlink_node_list():
    csv_filepath = os.path.join(os.getcwd(), 'data', 'winlink_node.csv')
    csv_tmp_filepath = os.path.join(os.getcwd(), 'data', 'tmp_winlink_node.csv')
    # Get updated list of winlink nodes
    api_key = 'BCFC301CD2E544A4A0DAD911248EB9AE'
    url = 'http://api.winlink.org/channel/list?key=' + api_key + '&format=json'
    response = requests.get(url)
    data = response.json()
    data = data['Channels']
    # Convert the JSON data to CSV
    keys = data[0].keys()
    with open(csv_tmp_filepath, 'w') as outfile:
        writer = csv.DictWriter(outfile, keys)
        writer.writeheader()
        writer.writerows(data)

    # Open the temp file and get rid of blank spaces.
    output = []
    with open(csv_tmp_filepath, 'r') as file:
        for row in file:
            output.append(row)
    # Check for/remove blank lines
    for line in range(len(output) - 1):
        if output[line] == '\n':
            output.pop(line)
    # write final CSV file.
    with open(csv_filepath, 'w') as outfile:
        for node in output:
            if output.index(node) != len(output) - 1:
                outfile.write(node)
            else:
                outfile.write(node.rstrip('\n'))


# provide list of Winlink nodes by frequency band and distance, closest -> farthest
