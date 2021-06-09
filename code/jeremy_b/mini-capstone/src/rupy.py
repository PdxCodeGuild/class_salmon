"""

Author: Jeremy Bush
Project: Radio Utilities in Python (RUPy)
Version: 1
Date: 6/8/2021

"""
"""

Application notes:

This solution is unique to Windows.  Mac and Linux systems have several applications that can perform this type of
function, however none exists for Windows.  

"""

# Import required libraries
import os  # needed to build paths
import serial  # needed to communicate with GPS unit
import pynmeagps  # needed to parse the information from the GPS
import requests  # required to download Winlink node list


# Read GPS coordinates from the GPS
def get_gps_coordinates(com_port='COM7'):
    # Open serial connection to the unit.  COM port may be different depending on each system.  Default is COM7
    stream = serial.Serial(com_port, 9600, timeout=3)
    nmr = pynmeagps.NMEAReader(stream)
    (raw_data, parsed_data) = nmr.read()  # raw_data is not used, but is required or error will result.
    return [round(parsed_data.lat, 6), round(parsed_data.lon, 6)]


# Convert GPS coordinates into grid square
def convert_to_grid(lat, lon):
    # adjust lat/lon per maidenhead calculation formula.  Followed the steps from here:
    # https://ham.stackexchange.com/questions/221/how-can-one-convert-from-lat-long-to-grid-square
    # The idea for using strings for upper/lower case letter strings came from Walter Underwood (K6WRU) based on his
    # Python script @ https://gist.github.com/laemmy/71ec20fd5d50a478e852618d94c16a8b
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWX'
    lower = 'abcdefghijklmnopqrstuvwx'

    lon += 180.0
    lat += 90.0

    # get remainder for sub square calculation.
    lon_remainder = (lon - int(lon / 2) * 2) * 60
    lat_remainder = (lat - int(lat)) * 60

    # Perform the actual calculation and return
    return upper[int(lon / 20)] + upper[int(lat / 10)] + str(int((lon / 2) % 10)) + str(int(lat % 10)) + \
           lower[int(lon_remainder / 5)] + lower[int(lat_remainder/2.5)]


# Update Winlink config file with new grid square
# Hard coded for now.  Need to convert this to a dynamic file path at some point.
def update_winlink_config(gridsquare):
    filepath = os.path.join('C:\\', 'RMS Express', 'RMS Express.ini')
    file = open(filepath, 'r')
    flag = 0
    index = 0
    search_text = 'Grid Square'
    for line in file:
        index += 1
        if search_text in line:
            flag = 1
            break


# download updated winlink node list
# provide list of Winlink nodes by frequency band and distance, closest -> farthest
