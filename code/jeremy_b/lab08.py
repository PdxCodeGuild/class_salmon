"""

Author: Jeremy Bush
Project: Programming Boot Camp Lab 08
Version: 1
Date: 5/24/2021

"""

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]


def peaks(data):
    peaks = []
    counter = 0
    while counter < len(data):
        if counter == 0:
            counter += 1
        elif counter == (len(data) - 1):
            counter += 1
        else:
            if data[counter] > data[counter - 1] and data[counter] > data[counter + 1]:
                peaks.append(data.index(data[counter]))
            counter += 1
    return peaks


def valleys(data):



print(peaks(data))
print(valleys(data))
