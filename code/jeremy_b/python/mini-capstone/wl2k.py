"""

Author: Jeremy Bush
Project: Radio Utilities in Python (RUPy), Winlink Express Utility Library
Version: 2
Date: 6/9/2021

"""


import os  # needed to build path
import requests
import shutil
import csv
import gps


# Update Winlink config file with new grid square
# Hard coded for now.  Need to convert this to a dynamic file path at some point.
def update_winlink_config(grid_square):
    filepath = os.path.join('C:\\', 'RMS Express', 'RMS Express.ini')
    # Create backup of config file prior to modifying
    shutil.copyfile(filepath, filepath+'.backup')
    # Read file for editing
    with open(filepath, 'r') as file:
        lines = file.read().split('\n')

    search_text = 'Grid Square'
    for line in range(len(lines) - 1):
        if search_text in lines[line]:
            lines[line] = 'Grid Square=' + grid_square
            break
    with open(filepath, 'w') as file:
        for line in range(len(lines) - 1):
            if line != len(lines) - 1:
                file.write(lines[line])
                file.write('\n')
            else:
                file.write(lines[line])


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
    # Check for/remove blank lines
    with open(csv_tmp_filepath, 'r') as file:
        for row in file:
            if row != '\n':
                output.append(row)
    # write final CSV file.
    with open(csv_filepath, 'w') as outfile:
        for node in output:
            if output.index(node) != len(output) - 1:
                outfile.write(node)
            else:
                outfile.write(node.rstrip('\n'))
    # remove the temp file:
    os.remove(csv_tmp_filepath)


# provide list of Winlink nodes by frequency band and distance, closest -> farthest
def get_close_nodes(gridsquare):
    # Open list of nodes and turn it into a list, then a list of dicts for searching
    # Eventually, CSV will be converted to a database that can be queried.

    user_qth = gridsquare

    node_list = []
    csv_filepath = os.path.join(os.getcwd(), 'data', 'winlink_node.csv')
    with open(csv_filepath, 'r') as file:
        for line in file:
            node_list.append(line.split(','))

    keys = [node_list[0][1], node_list[0][3], node_list[0][4], node_list[0][5], node_list[0][6]]
    node_list.pop(0)
    station_info = [{keys[0]: node_list[line][1], keys[1]: node_list[line][3], keys[2]: int(node_list[line][4]),
                     keys[3]: int(node_list[line][5]),
                     keys[4]: int(node_list[line][6]),
                     "Distance": round(gps.get_geo_distance(user_qth, node_list[line][3]))}
                    for line in range(len(node_list) - 1)]
    return station_info


def get_close_nodes_by_mode(mode):
    # dict of modes for future use
    modes = {
        0: "Packet 1200",
        1: "Packet 2400",
        2: "Packet 4800",
        3: "Packet 9600",
        4: "Packet 19200",
        5: "Packet 38400",
        11: "Pactor 1",
        12: "Pactor 1, 2",
        13: "Pactor 1, 2, 3",
        14: "Pactor 2",
        15: "Pactor 2, 3",
        16: "Pactor 3",
        17: "Pactor 1, 2, 3, 4",
        18: "Pactor 2, 3, 4",
        19: "Pactor 3, 4",
        20: "Pactor 4",
        21: "WINMOR 500",
        22: "WINMOR 1600",
        30: "Robust Packet",
        40: "ARDOP 200",
        41: "ARDOP 500",
        42: "ARDOP 1000",
        43: "ARDOP 2000",
        44: "ARDOP 2000 FM",
        50: "VARA",
        51: "VARA FM",
        52: "VARA FM WIDE",
        53: "VARA 500",
        54: "VARA 2750"
    }

    station_list = get_close_nodes(gps.get_current_grid_square())
    close_by_mode = []
    for station in range(len(station_list) - 1):
        if station_list[station]['Mode'] == mode:
            close_by_mode.append(station_list[station])

    close_by_mode = sorted(close_by_mode, key=lambda item: item['Distance'])

    return [close_by_mode[station] for station in range(0, 24)]
