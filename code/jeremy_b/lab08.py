"""

Author: Jeremy Bush
Project: Programming Boot Camp Lab 08
Version: 1
Date: 5/24/2021

"""

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
peaks = []
valleys = []
counter = 0

while counter != len(data):
    if counter > 0:
        if data[counter] > data[counter - 1] and data[counter] > data[counter + 1]:
            peaks.append(data[counter])
        elif data[counter] < data[counter - 1] and data[counter] < data[counter + 1]:
            valleys.append(data[counter])
        counter += 1
    else:
        counter += 1
