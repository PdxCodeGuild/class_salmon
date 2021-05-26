"""

Author: Jeremy Bush
Project: Programming Boot Camp Lab 10
Version: 1
Date: 5/26/2021

"""

import os


def parse_contacts(filename):
    # Read from the CSV to a list of lists, one list per contact.
    with open(filename, 'r') as file:
        lines = file.read().split('\n')
    # Convert each list into a list of its own
    lines = [line.split(',') for line in lines]
    # convert each list in lines to a dictionary and add to contacts
    contacts = [{'name': i[0], 'fav_fruit': i[1], 'fav_color': i[2]} for i in lines]

    return contacts


# Get file name for contacts list.  This is only needed on initial startup.  The same file will be used until the
# program is restareted.
try:
    file = os.path.join(os.getcwd(), input("Please contacts filename with extension: "))
    if file:
        contacts = parse_contacts(file)
    else:
        raise FileNotFoundError
except FileNotFoundError:
    print("File not found.")

# Loop for menu options.

